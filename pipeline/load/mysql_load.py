import mysql.connector
import pandas as pd
import ast

DB_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "2040",
    "database" : "job_analytics"
}

FILE_PATH = "C:/job-market-analytics/data/clean/jobs_clean.csv"

def load_to_mysql():
    df = pd.read_csv(FILE_PATH)

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO jobs (title, company, location, scraped_at, skills)
        VALUES (%s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        skills = row["skills"]
        if isinstance(skills, str):
            skills = skills.replace('[', "").replace("]","").replace("'","")

        cursor.execute(
            insert_query, (
                row["title"],
                row["company"],
                row['location'],
                row['scraped_at'],
                skills
            )
        )
    
    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded into MYSQL database")

if __name__ == "__main__":
    load_to_mysql()