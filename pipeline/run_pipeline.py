import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXEC = sys.executable

def run(step):
    print(f"Running{step}")
    subprocess.run([PYTHON_EXEC, step], check=True)

if __name__ == "__main__":
    run(os.path.join(BASE_DIR, "extract","scraper.py"))
    run(os.path.join(BASE_DIR, "transform","clean.py"))
    run(os.path.join(BASE_DIR, "load","mysql_load.py"))

    print("ETL Pipeline completed Successfully")