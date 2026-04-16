# Medicine Supply Chain Disruption Predictor

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green)
![XGBoost](https://img.shields.io/badge/XGBoost-3.2-orange)
![Docker](https://img.shields.io/badge/Docker-Containerised-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![Render](https://img.shields.io/badge/Render-Live-brightgreen)

##  Live Demo
**API URL:** https://medicine-supply-predictor.onrender.com/docs

An end-to-end ML system that predicts which medicines are at risk 
of supply chain disruption using real FDA drug shortage data.

##  Project Overview

This project builds a complete ML pipeline to predict medicine supply 
chain disruptions using real FDA drug shortage data. It combines 
data science, machine learning, and DevOps into one end-to-end system.

**Problem:** Drug shortages cost lives. Hospitals need early warning 
systems to identify which medicines are at risk before they run out.

**Solution:** An ML model trained on real FDA shortage data that predicts 
risk level for any drug based on supply chain indicators.

##  Tech Stack

| Component | Technology |
|---|---|
| Data Source | Real FDA Drug Shortage API (1703 records) |
| ML Model | XGBoost Classifier |
| API Framework | FastAPI |
| Containerisation | Docker |
| CI/CD Pipeline | Jenkins |
| Deployment | Render (free cloud) |
| Dashboard | Power BI |
| Language | Python 3.13 |

## ✨ Key Features

- **Real FDA Data** — 1703 real drug shortage records from OpenFDA API
- **ML Prediction** — XGBoost model predicts At Risk vs Not At Risk
- **Live API** — FastAPI endpoint accessible via public URL
- **Auto Deploy** — Jenkins pipeline rebuilds and redeploys on every push
- **Docker** — Fully containerised, runs anywhere with one command
- **Dashboard** — Interactive Power BI dashboard with 6 visuals

## 🧠 ML Details

**Dataset:** Real FDA Human Drug Shortages data (2012-2026)

**Features used:**
- Production drop in last 3 months (%)
- Import dependency ratio (%)
- Demand surge indicator
- Days since last shortage
- Manufacturer shortage history
- Price increase percentage

**Model:** XGBoost Classifier
- Accuracy: 56% (honest result after removing 6 sources of data leakage)
- Handled class imbalance with scale_pos_weight
- Key finding: Identified data leakage in update_type, shortage_reason, 
  year columns — all directly correlated with target variable

## 🏗️ Architecture

```
Real FDA Data → Data Cleaning → Feature Engineering
→ XGBoost Model → FastAPI → Docker Container
→ Jenkins CI/CD → Render Cloud Deployment
→ Power BI Dashboard
```

## 📊 Key Findings from EDA

- **1703 real drug shortage records** from FDA (2012-2026)
- **35.2% of drugs are At Risk** of supply chain disruption
- **2025 had the highest shortages ever** — 433 cases
- **Demand increase** is the most common shortage reason
- **Anesthesia and Psychiatry** are the most affected categories
- Identified and removed **6 sources of data leakage** during ML development

## 🤖 ML Model Performance

| Metric | Score |
|---|---|
| Model | XGBoost Classifier |
| Accuracy | 56% (honest, no data leakage) |
| Features | 6 supply chain indicators |
| Training data | 1362 records |
| Test data | 341 records |

> Note: 100% accuracy was achieved initially but identified as data 
> leakage. 6 leaky features were removed for honest evaluation.




## 🚀 How to Run Locally

### Option 1 — Docker (recommended)
```bash
docker pull your-dockerhub-username/medicine-predictor
docker run -p 8000:8000 medicine-predictor
```
Then open: http://localhost:8000/docs

### Option 2 — Python
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📡 API Usage

**Endpoint:** POST /predict

**Example Request:**
```json
{
  "production_drop_3m": 75.0,
  "import_dependency": 90.0,
  "demand_surge": 1,
  "days_since_last_shortage": 30.0,
  "manufacturer_shortage_history": 12.0,
  "price_increase_pct": 70.0
}
```

**Example Response:**
```json
{
  "prediction": "At Risk",
  "confidence": "68.5%",
  "risk_score": 1
}
```

## 👤 Author
**Neha Madrala**
- GitHub: https://github.com/nehaM906
- Live API: https://medicine-supply-predictor.onrender.com/docs