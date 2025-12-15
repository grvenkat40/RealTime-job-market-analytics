import pandas as pd
import json
import re

RAW_Path = "C:/job-market-analytics/data/raw/jobs_raw.json"
CLEAN_Path = "C:/job-market-analytics/data/clean/jobs_clean.csv"

Skills_keywords = [
    "python", "django", "flask", "fastapi", "sql", "mysql", "postgres",
    "aws", "azure", "gcp", "pandas", "numpy", "git", "docker"
]

def extract_skills(title):
    if not isinstance(title, str):
        return []
    
    skills = []
    for skill in Skills_keywords:
        if re.search(rf"\b{skill}\b" , title.lower()):
            skills.append(skill)
    
    return skills

def clean_data():
    with open(RAW_Path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)

    df['company'] = df["company"].str.strip()
    df['location'] = df["location"].str.replace("\n"," ",regex=False).str.strip()

    df.drop_duplicates(subset=['title', 'company', 'location'], inplace=True)

    df["skills"] = df['title'].apply(extract_skills)
    df.to_csv(CLEAN_Path, index=False)

    # print(f'Cleaned data saved -> {CLEAN_Path}')
    print(f'Total clean rows:{len(df)}')

if __name__ == "__main__":
    clean_data()