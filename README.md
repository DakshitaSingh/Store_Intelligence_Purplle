# Store Intelligence Platform

## Overview

Store Intelligence Platform converts CCTV footage into retail business insights.

The system processes CCTV video streams, generates behavioral events, stores them in a database, computes analytics, and exposes insights through APIs and an interactive dashboard.

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

## Architecture

```text
Video Streams
      |
      v
Detection & Tracking
      |
      v
Event Generation
      |
      v
FastAPI Ingestion API
      |
      v
SQLite Database
      |
      +-------------------+
      |                   |
      v                   v
Analytics Engine     Health Monitoring
      |
      v
Streamlit Dashboard
```

---

## Project Structure

```text
app/
dashboard/
detection/
data/
tests/
README.md
DESIGN.md
CHOICES.md
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

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

API URL:

```text
http://127.0.0.1:8000
```

---

## Running Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://127.0.0.1:8501
```

---

## Detection Pipeline

Store 1:

```bash
cd detection

python process_store.py
```

Store 2 / Multi-Camera:

```bash
cd detection

python process_multicam.py
```

---

## Replay Events

```bash
python event_replayer.py
```

Multi-camera replay:

```bash
python replay_multicam.py
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

## Event Schema

Generated event logs follow JSONL format.

Supported event types:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL
* BILLING_QUEUE_JOIN

Each event contains:

* event_id
* store_id
* camera_id
* visitor_id
* event_type
* timestamp
* zone_id
* dwell_ms
* is_staff
* confidence
* metadata

---

## Docker Deployment

Build:

```bash
docker-compose build
```

Run:

```bash
docker-compose up
```

API:

```text
http://localhost:8000
```

Dashboard:

```text
http://localhost:8501
```

---

## Testing

Run tests:

```bash
pytest
```

Current Status:

```text
4 passed
```

---

## Validation

Validated Components:

* Event ingestion
* Metrics API
* Funnel API
* Health API
* Dashboard integration
* Docker deployment

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

## requirements.txt

Contains full development dependencies including computer vision libraries used during event generation.

---

## requirements-docker.txt

Contains lightweight runtime dependencies used for API and dashboard deployment.

Large training and inference dependencies are excluded to reduce Docker image size and build time.

---

## Dataset

As required by the challenge guidelines:

Excluded from repository:

* CCTV videos
* Raw datasets
* POS source files
* Store layout assets

Included in repository:

* Generated JSONL event logs required for evaluation

The application remains functional once the challenge assets are placed in the expected data directories.

---

## Future Enhancements

* Real-time streaming
* Multi-store analytics
* Cross-camera re-identification
* Kafka event streaming
* PostgreSQL migration
* Advanced anomaly detection

## Event Logs

Generated event logs are available in:

data/generated_events/

Files:
- store1_events.jsonl
- multicam_events.jsonl
- submission_events.jsonl

## submission_events.jsonl is the final schema-compatible event log generated for challenge submission.
