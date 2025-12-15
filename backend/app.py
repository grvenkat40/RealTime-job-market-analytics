from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.analytics import top_skills, jobs_by_location, hiring_companies
from backend.analytics import get_jobs
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
    location : Optional[str] = None,
    skill : Optional[str] = None
):
    return get_jobs(page, limit, role, location, skill)