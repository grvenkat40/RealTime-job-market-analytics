from fastapi import FastAPI,BackgroundTasks, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pipeline.extract.scraper import scrape_jobs
from pipeline.transform.clean import clean_data
from backend.analytics import (
    top_skills, 
    jobs_by_location, 
    hiring_companies,
    get_jobs
)
from backend.db import insert_jobs
from typing import Optional

app = FastAPI(title="Job Market Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def root():
    return {"Status" : "API is Live"}

@app.get("/analytics/skills")
def skills():
    return top_skills()

@app.get("/analytics/locations")
def locations():
    return jobs_by_location()

@app.get("/analytics/companies")
def companies():
    return hiring_companies()

@app.get("/jobs")
def jobs(
    page : int =1,
    limit : int =10,
    role :Optional[str] = None,
    location : Optional[str] = None
):
    return get_jobs(page, limit, role, location)

# API_KEY = os.getenv("API_KEY")

@app.post("/scrape")
def trigger_scrape(payload:dict, background_tasks : BackgroundTasks):
    # if x_api_key != API_KEY:
    #     raise HTTPException(status_code=403, detail="Invalid API Key")

    role = payload.get("role")
    city = payload.get("city", "")

    if not role:
        return {"error": "role is required"}

    def run_pipeline():
        raw_jobs = scrape_jobs(role, city)
        cleaned_jobs = clean_data(raw_jobs)
        insert_jobs(cleaned_jobs)

    background_tasks.add_task(run_pipeline)

    return {
        "status" : "started",
        "role" : role,
        "city" : city
    }
