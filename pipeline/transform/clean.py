import json
import re
import random

# RAW_Path = "C:/job-market-analytics/data/raw/jobs_raw.json"
# CLEAN_Path = "C:/job-market-analytics/data/clean/jobs_clean.csv"

SKILL_KEYWORDS = {
    "Data Engineer": [
        "sql", "python", "spark", "pyspark", "hadoop", "airflow", 
        "kafka", "aws", "azure", "gcp", "snowflake", "redshift", 
        "bigquery", "etl", "elt", "databricks", "docker", "kubernetes"
    ],

    "Python Developer": [
        "python", "django", "flask", "fastapi", "sql", "orm", 
        "sqlalchemy", "rest api", "git", "docker", "linux", 
        "postgresql", "mysql", "redis", "celery", "pytest"
    ],

    "Data Analyst": [
        "sql", "excel", "python", "pandas", "numpy", "tableau", 
        "power bi", "looker", "statistics", "data visualization", 
        "matplotlib", "seaborn", "r", "sas"
    ],

    "Frontend Developer": [
        "javascript", "typescript", "react", "angular", "vue", 
        "html", "css", "tailwind", "bootstrap", "redux", 
        "nextjs", "webpack", "figma", "git"
    ],

    "DevOps Engineer": [
        "linux", "aws", "azure", "docker", "kubernetes", "jenkins", 
        "terraform", "ansible", "ci/cd", "bash", "shell scripting", 
        "prometheus", "grafana", "git", "circleci"
    ]
}

def extract_skills(text : str):
    if not isinstance(text, str):
        return []
    
    text = text.lower()
    found_skills = []
    for role_skill in SKILL_KEYWORDS.values():
        for skill in role_skill:
            if re.search(rf"\b{re.escape(skill)}\b" , text):
                found_skills.append(skill)
    
    return list(found_skills)

def clean_data(raw_jobs:list[dict]) -> list[dict]:
    seen = set()
    cleaned = []

    for job in raw_jobs:
        title = job.get("title", "").strip()
        company = job.get("company","").strip()
        location = job.get("location","").replace("\n", " ").strip()

        key = (title, company, location)

        if key in seen:
            continue
        seen.add(key)

        skills = extract_skills(title)

        cleaned.append({
            "title" : title,
            "company" :company,
            "location" :location,
            "role" : job.get("role"),
            "city" : job.get("city"),
            "skills" : ",".join(skills),
            "scraped_at" : job.get("scraped_at")
        })
    return cleaned