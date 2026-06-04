# Store Intelligence Platform

## Overview

Store Intelligence Platform converts CCTV footage into retail business insights.

The system processes video streams, generates customer behavioral events, stores them, computes analytics, and exposes insights through APIs and dashboards.

---

## Features

* Visitor Detection
* Visitor Tracking
* Event Generation
* Conversion Funnel Analytics
* Heatmap Analytics
* Operational Anomaly Detection
* Health Monitoring
* Streamlit Dashboard
* Multi-Camera Support

---

## Project Structure

```text
app/
dashboard/
detection/
data/
tests/
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running API

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

---

## Running Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Detection Pipeline

```bash
cd detection

python process_store.py
```

---

## Replay Events

```bash
python event_replayer.py
```

---

## Available Endpoints

### Health

```text
GET /health
```

### Metrics

```text
GET /stores/{store_id}/metrics
```

### Funnel

```text
GET /stores/{store_id}/funnel
```

### Heatmap

```text
GET /stores/{store_id}/heatmap
```

### Anomalies

```text
GET /stores/{store_id}/anomalies
```

### Event Ingestion

```text
POST /events/ingest
```

---

## Testing

```bash
pytest
```

Current status:

```text
4 passed
```

---

## Technology Stack

* Python
* FastAPI
* SQLite
* Streamlit
* OpenCV
* Pandas
* SQLAlchemy

---

## Future Enhancements

* Real-time streaming
* Multi-store analytics
* Camera re-identification
* Kafka integration
* PostgreSQL migration

## requirements.txt:
Contains full development dependencies including
computer vision libraries used during event generation.

## requirements-docker.txt:
Contains lightweight runtime dependencies used for
API and dashboard deployment. This avoids shipping
large model packages such as torch inside the
container and significantly reduces build time.

## Dataset

Challenge datasets, CCTV videos, POS files, generated events, and store layout assets are excluded from this repository as required by the submission guidelines.

The application remains functional once the provided challenge assets are placed in the expected data directories.
