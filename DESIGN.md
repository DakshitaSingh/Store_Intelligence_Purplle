# Store Intelligence System Design

## Overview

The objective of this system is to transform raw CCTV footage into actionable retail analytics. The platform processes store video feeds, generates behavioral events, stores them in a database, and exposes business metrics through APIs and a dashboard.

---

## System Architecture

```text
Video Streams
      |
      v
Detection & Tracking Layer
      |
      v
Event Generation Layer
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
Dashboard
```

---

## Components

### 1. Detection Layer

Responsible for detecting customers in CCTV footage.

Functions:

* Person detection
* Visitor tracking
* Multi-camera processing
* Zone assignment

Outputs:

* Visitor identifiers
* Location information
* Tracking information

---

### 2. Event Generation Layer

Transforms detections into structured behavioral events.

Generated events:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL
* BILLING_QUEUE_JOIN

Each event contains:

* Event ID
* Visitor ID
* Store ID
* Camera ID
* Timestamp
* Zone
* Metadata

---

### 3. Event Ingestion API

Receives events and stores them in the database.

Responsibilities:

* Validation
* Deduplication
* Persistence

---

### 4. Analytics Layer

Computes retail intelligence metrics.

Supported analytics:

* Visitor count
* Conversion rate
* Dwell time
* Funnel analysis
* Heatmaps
* Operational anomalies

---

### 5. Dashboard Layer

Visualizes analytics using Streamlit.

Displays:

* KPI metrics
* Conversion funnel
* Zone heatmap
* Store anomalies
* System health

---

## Data Flow

```text
Video
→ Detection
→ Tracking
→ Event Creation
→ API Ingestion
→ Database
→ Analytics
→ Dashboard
```

---

## Scalability Considerations

The system uses an event-driven architecture which allows future migration from SQLite to PostgreSQL and from local processing to distributed deployment with minimal changes.

## Assumptions

The challenge provides CCTV footage but does not provide
ground truth visitor identities.

The following assumptions were made:

- Every tracked person corresponds to a visitor.
- Billing area activity is used as a proxy for purchase intent.
- Zone boundaries are approximated using normalized frame coordinates.
- Event replay simulates near real-time operation.
- Visitor identifiers are local to a camera session.

## Multi-Store Support

The system was validated on multiple store layouts.

Store 1:
- Entry camera processing
- Zone analytics

Store 2:
- Multi-camera processing
- Billing area monitoring
- Queue analytics

This demonstrates that the architecture generalizes across stores with different layouts and camera placements.

## AI-Assisted Decisions

AI assistance was used during the development process to accelerate implementation and documentation.

Areas where AI assistance was utilized:

- API structure and endpoint organization
- Documentation drafting and formatting
- Dockerization guidance
- Dashboard layout suggestions
- Event schema refinement
- Testing and validation recommendations

All architectural decisions, business logic, analytics definitions, event generation logic, and implementation details were reviewed, modified, and validated by the author before inclusion in the final solution.

The final system design, engineering trade-offs, and business metrics reflect independent engineering decisions made during project development.