from fastapi import (
    FastAPI,
    Depends,
    Request
)
import time

from app.logger import logger


from sqlalchemy.orm import Session

from app.database import (
    engine,
    SessionLocal,
    Base
)
from app.middleware import (
    log_requests
)
from app.revenue import (
    revenue_metrics
)
from app.queue_metrics import (
    get_queue_metrics
)
from app.journey import (
    get_journey
)
from app.store_compare import (
    compare_stores
)

from app.models import Event

from app.ingestion import ingest_events

from app.metrics import get_store_metrics

from app.funnel import build_funnel

from app.health import get_health

from app.load_pos import load_transactions

from app.anomalies import get_anomalies

from app.heatmap import get_heatmap


Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    load_transactions(db)
finally:
    db.close()


app = FastAPI(
    title="Store Intelligence API"
)
@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):

    start = time.time()

    response = await call_next(
        request
    )

    duration = round(
        time.time() - start,
        3
    )

    logger.info(

        f"{request.method} "

        f"{request.url.path} "

        f"status={response.status_code} "

        f"time={duration}s"
    )

    return response
app.middleware(
    "http"
)(
    log_requests
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
@app.get(
"/stores/{store_id}/revenue"
)
def revenue(
    store_id: str
):

    db = SessionLocal()

    result = revenue_metrics(
        db,
        store_id
    )

    db.close()

    return result
@app.get(
"/stores/{store_id}/queue"
)
def queue_metrics(
    store_id: str
):

    db = SessionLocal()

    result = get_queue_metrics(
        db,
        store_id
    )

    db.close()

    return result
@app.get("/")
def root():

    return {
        "service": "store-intelligence"
    }


@app.post("/events/ingest")
def ingest(
    events: list[Event]
):

    db = SessionLocal()

    result = ingest_events(
        db,
        events
    )

    db.close()

    return result


@app.get(
    "/stores/{store_id}/metrics"
)
def metrics(
    store_id: str
):

    db = SessionLocal()

    result = get_store_metrics(
        db,
        store_id
    )

    db.close()

    return result


@app.get(
    "/stores/{store_id}/funnel"
)
def funnel(
    store_id: str
):

    db = SessionLocal()

    result = build_funnel(
        db,
        store_id
    )

    db.close()

    return result


@app.get(
    "/stores/{store_id}/heatmap"
)
def heatmap(
    store_id: str,
    db: Session = Depends(get_db)
):

    return get_heatmap(
        db,
        store_id
    )


@app.get(
    "/stores/{store_id}/anomalies"
)
def anomalies(
    store_id: str,
    db: Session = Depends(get_db)
):

    return get_anomalies(
        db,
        store_id
    )


@app.get("/health")
def health(
    db: Session = Depends(get_db)
):

    return get_health(
        db
    )
@app.get(
"/compare"
)
def compare():

    db = SessionLocal()

    result = compare_stores(
        db,
        [
            "ST1008",
            "STORE_2"
        ]
    )

    db.close()

    return result
@app.get(
"/visitors/{visitor_id}/journey"
)
def journey(
    visitor_id: str
):

    db = SessionLocal()

    result = get_journey(
        db,
        visitor_id
    )

    db.close()

    return result