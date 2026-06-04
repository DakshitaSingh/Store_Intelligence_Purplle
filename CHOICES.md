# Engineering Decisions and Trade-offs

## 1. Event Driven Architecture

### Choice

Behavioral events are generated first and analytics are computed later.

### Reason

This decouples video processing from business analytics.

### Trade-off

Additional storage overhead for event persistence.

---

## 2. SQLite Database

### Choice

SQLite was selected for persistence.

### Reason

Simple setup and portability.

### Trade-off

Not suitable for extremely high-volume production workloads.

---

## 3. Lightweight Detection Pipeline

### Choice

Use lightweight person detection and tracking.

### Reason

Challenge focuses on system design rather than detection accuracy.

### Trade-off

Detection accuracy may be lower than large production-grade models.

---

## 4. Zone-Based Store Analytics

### Choice

Store divided into logical zones.

### Reason

Enables heatmap generation and customer flow analysis.

### Trade-off

Zone boundaries are approximations.

---

## 5. Event Replay Architecture

### Choice

Generated events are replayed into the API.

### Reason

Simulates real-time streaming without requiring live deployment.

### Trade-off

Replay latency differs from actual production streams.

---

## 6. Billing Queue Monitoring

### Choice

Queue events generated near billing areas.

### Reason

Provides operational insights beyond visitor counting.

### Trade-off

Queue estimation uses heuristics rather than dedicated queue models.

---

## 7. Streamlit Dashboard

### Choice

Streamlit selected for visualization.

### Reason

Rapid development and easy deployment.

### Trade-off

Less customizable than enterprise BI tools.

---

## Future Improvements

* Re-identification across cameras
* PostgreSQL backend
* Kafka event streaming
* Real-time WebSocket updates
* Advanced anomaly detection
* Store layout calibration

## Known Limitations

- Cross-camera re-identification is not implemented.
- Staff members are not explicitly filtered.
- Queue estimation is heuristic based.
- Conversion rate uses transaction count rather than customer-level purchases.
- Tracking quality depends on CCTV visibility and occlusions.
