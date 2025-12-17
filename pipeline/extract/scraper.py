# from backend.db import insert_jobs
from playwright.sync_api import sync_playwright
import json
from datetime import datetime

def scrape_jobs(role:str, city:str):
    search_role = role.replace(" ","+")
    search_city = city.replace(" ","+")

    url = furl = f"https://in.indeed.com/jobs?q={search_role}&l={search_city}"
    print(f"DEBUG: Navigating to {url}")
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        # url = "https://www.indeed.com/jobs?q=python+developer&l="
        try:
            page.goto(url, timeout=60000)
            # page.wait_for_selector(".job_seen_beacon")
            page.wait_for_selector(".job_seen_beacon", timeout=10000)
            job_cards = page.locator(".job_seen_beacon")
            count = job_cards.count()

            if count == 0:
                print("No job cards found - possibly blocked or no results")
            else:
                print(f"✅ Found {count} jobs.")
            for job in job_cards.all():
                title_el = job.locator("h2.jobTitle span").first
                company_el = job.locator("[data-testid='company-name']").first
                location_el = job.locator("[data-testid='text-location']").first

            

                results.append({
                    "title" : title_el.inner_text() if title_el.count() > 0 else "Unknown",
                    "company" : company_el.inner_text() if company_el.count() > 0 else "Unknown",
                    "location" : location_el.inner_text() if location_el.count() > 0 else "Unknown",
                    "role" : role,
                    "city" : city,
                    "scraped_at" : datetime.now().isoformat()   
                })
                print(f"-> ✅ Scraped:{"title"}")
        except Exception as e:
            print(f"❌ Error during scraping: {e}")
        finally:
            browser.close()

    return results

# scrape_jobs("python", "chennai")
# if __name__ == "__main__":
#     data = scrape_jobs()
#     # with open("C:/job-market-analytics/data/raw/jobs_raw.json", 'w') as f:
#         # json.dump(data, f, indent=4)
#     if data:
#         insert_jobs(data)
#     print(f"Scraped {len(data)} jobs!")
