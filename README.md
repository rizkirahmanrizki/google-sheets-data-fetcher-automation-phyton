# 📊 Google Sheets Data Fetcher (Python)

A scalable Python-based automation pipeline to fetch data from **Metabase (or any BI API)** and write it into **Google Sheets**, designed for large datasets and production workloads.

---

## 🚀 Features

* Fetch data from BI tools via API (Metabase-ready)
* Handle large datasets (chunking-friendly structure)
* Write structured data to Google Sheets
* Dynamic date range (weekly automation)
* Column filtering & schema control
* Optional Google Chat notifications
* Secure credential handling via environment variables

---

## 🧩 Tech Stack

* Python 3.10+
* Google Sheets API
* Requests
* dotenv (for secrets management)

---

## 📁 Project Structure

```
src/
  main.py          # Entry point
  config.py        # Environment config
  sheets.py        # Google Sheets logic
  metabase.py      # API fetch logic
  utils.py         # Helpers

.env.example
requirements.txt
README.md
```

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone https://github.com/your-repo/google-sheets-data-fetcher-python.git
cd google-sheets-data-fetcher-python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup environment

```bash
cp .env.example .env
```

Fill in all required values.

---

## 🔐 Security Notes

* Never commit `.env`
* Service account keys must stay private
* Use environment variables in production (CI/CD, Docker, etc.)

---

## ▶️ Run

```bash
python src/main.py
```

---

## 📈 Use Cases

* BI → Google Sheets sync
* Weekly reporting automation
* Operational dashboards
* Lightweight ETL pipelines

---

## 🚀 Future Improvements

* Parallel job execution
* Pandas transformations
* Docker deployment
* Scheduler (cron / Airflow)

---

## 🧠 Summary

This project is essentially a **lightweight ETL pipeline**:

> Metabase API → Python Processing → Google Sheets → Notification

Designed for scalability beyond Google Apps Script limitations.
