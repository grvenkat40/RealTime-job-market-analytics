import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
from pipeline.extract.scraper import scrape_jobs
from pipeline.transform.clean import clean_data
from backend.db import insert_jobs

def run_pipeline(role, city):
    print("Step-1:Scraping Strated...wait")
    raw_jobs = scrape_jobs(role, city)
    print("Step-2:Cleaning Strated...wait")
    cleaned_jobs = clean_data(raw_jobs)
    print("Step-3:Loading Strated...wait")
    insert_jobs(cleaned_jobs)
    print("ETL Pipeline completed Successfully")

role = "python"
city = "Chennai"
run_pipeline(role, city)