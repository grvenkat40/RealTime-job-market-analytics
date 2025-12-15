from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json
from datetime import datetime

def scrape_jobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        url = "https://www.indeed.com/jobs?q=python+developer&l="
        #Dynamic - f"https://www.indeed.com/jobs?q={role}&l={city}"
        page.goto(url, timeout=60000)
        page.wait_for_selector(".job_seen_beacon")
        job_cards = page.query_selector_all(".job_seen_beacon")

        results = []
        for job in job_cards:
            title_el = job.query_selector("h2.jobTitle span")
            company_el = job.query_selector("[data-testid='company-name']")
            location_el = job.query_selector("[data-testid='text-location']")

            results.append({
                "title" : title_el.inner_text() if title_el else "Unknown",
                "company" : company_el.inner_text() if company_el else "Unknown",
                "location" : location_el.inner_text() if location_el else "Unknown",
                "scraped_at" : datetime.now().isoformat()   
            })

        browser.close()
        return results

if __name__ == "__main__":
    data = scrape_jobs()
    with open("C:/job-market-analytics/data/raw/jobs_raw.json", 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Scraped {len(data)} jobs!")
