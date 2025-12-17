# 📊 Real-Time Job Market Analytics

A Full-stack, cloud-deployed application that scrapes live jobs postings on demand, processes then through an ETL pipeline, and visualize real-time job market trends using interactice dashboards. 
---

## 🚀 Project Overview 

- Real-Time Job Market Analytics enables users to search for jobs by roles and location , dynamically triggers web scraping, and analyze hiring trends such as top companies, location, and in-demand skills.
- The system follows a decoupled, production-grade architecture with separate frontend, backend, scraping pipeline and cloud database.

## 🏗️ System Architecture

```text
Frontend (Netlify)
   |
   |  REST API Calls
   v
Backend API (FastAPI – Render)
   |
   |  Background Task
   v
Web Scraper (Playwright)
   |
   v
Transform Layer (Skill Extraction + Deduplication)
   |
   v
Database (TiDB Cloud – MySQL Compatible)

```
## 🧩 Key Features
- 🔍 User-Driven job search (role & city)
- 🌐 On-demand web scraping using playwight
- 🔄 ETL pipeline (Extract -> Transform -> Load)
- 🧠 Skill extraction fron job titles
- 📊 Interactive analytical dashboards (Chart.js)
- ☁️ Cloud-native deployment
- 🧱 Decoupled frontend & backend

## 🛠️ Tech Stack
**Backend**
- FastAPI
- Python
- Playwright (web scraping)
- MySQL (Connector)
- 
**Database**
- TiDB Cloud (serverless MySQL - compatible database)
- 
**Frontend**
- HTML
- CSS
- JavaScript
- Chart.js
  
**Deployment**
- Render -> Backend API
- Netlify -> Frondend
- GitHub -> Version control

## 📂 Project Structure
```text
.
├── backend/
│   ├── app.py              # FastAPI entry point
│   ├── analytics.py        # SQL-based analytics logic
│   ├── db.py               # Database connection & inserts
│   └── __init__.py
│
├── pipeline/
│   ├── extract/
│   │   └── scraper.py      # Playwright scraper
│   ├── transform/
│   │   └── clean.py        # Skill extraction & cleaning
│   └── run_pipeline.py
│
├── frontend/
│   ├── index.html
│   └── static/
│       ├── css/
│       └── js/
│
├── requirements.txt
└── README.md

```

## 🔄 Data Flow (ETL)
1. Extract
  - Scrape job listings from Indeed using Playwright.
  - Triggered only when the user submits a search.
  
2. Transform
  - Clean text data
  - Remove duplicates
  - Extract technical skills using keyword matching

3. Load
  - Store structured data in TidDB Cloud
  - Optimized for analytics queries

# 🔌 API Endpoints

Health Check
```text
GET /
```
Trigger Scraping
```text
POST /scrape
```
Payload
```text
{
  "role": "python developer",
  "city": "bangalore"
}
```
Analytics
```text
GET /analytics/locations
GET /analytics/companies
GET /analytics/skills
```
Paginated Job Listings
```text
GET /jobs?page=1&limit=10&role=python&location=india
```
## 🌐 Live Deployment
- Backend API: Render
- Fronend Dashboard : Netlify
- Database : TiDB cloud
The frontend communicates with the backend via REST APIs, following a fully decoupled deployment model.

## 🔐 Design Decisions
* Scraping runs only on demand, not continuously
* Background tacks prevent blocking API response
* No scraping logic runs at server startup
* Cloud-safe database connections with environment variables
* CORS enabled for cross-origin frontend access

## 🧪 How to Run Locally
**Backend**
```text
pip install -r requirements.txt
```
```text
uvicorn backend.app:app --reload
```
**Frontend**

Open frontend/index.html directly in the browser
(or serve with a simple static server)

## 📈 Future Enhancements

- Job description scraping
- Skill frequency trends over time
- Authentication for scrape endpoint
- Rate limiting & retry logic
- Dockerized deployment
- Support for multiple job boards

## 🧾 Resume Highlight

Built a real-time job market analytics platform using FASTAPI, Playwright, and TiDB Cloud with an on-demand ETL pipeline and interative frontend dashboard.
Deployed a decoupled cloud architecture with backend services on Render and Frontend on Netlify.

## 🧠 Final Note
This project demonstrate backend engineering, data engineering, cloud deployment and frontend integration
in a single system -- designed and implemented ene-to-end.

