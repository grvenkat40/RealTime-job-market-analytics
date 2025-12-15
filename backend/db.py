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
        port = int(os.getenv("DB_PORT")),
        ssl_disabled=False

        # host = "localhost",
        # user = "root",
        # password = "2040",
        # database = "job_analytics"
    )