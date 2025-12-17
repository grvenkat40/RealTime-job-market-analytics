import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connections():
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME","job_analytics"),
        port = int(os.getenv("DB_PORT", 4000)),
        ssl_disabled=False

        # host = "localhost",
        # user = "root",
        # password = "2040",
        # database = "job_analytics"
    )

def insert_jobs(jobs):
    if not jobs:
        return
    conn = get_connections()
    cursor = conn.cursor()

    query ="""
    INSERT INTO jobs(title, company, location, role, city, skills,scraped_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = [
        (
            job["title"],
            job["company"],
            job["location"],
            job["role"],
            job["city"],
            job["skills"],
            job["scraped_at"]
        )
        for job in jobs
    ]
    cursor.executemany(query, values)
    conn.commit()

    cursor.close()
    conn.close()