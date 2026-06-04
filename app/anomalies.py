from sqlalchemy import func

from app.schema import (
    EventTable,
    TransactionTable
)


def detect_anomalies(
    db,
    store_id
):

    anomalies = []

    visitors = db.query(
        func.count(
            func.distinct(
                EventTable.visitor_id
            )
        )
    ).filter(
        EventTable.store_id == store_id
    ).scalar() or 0

    transactions = db.query(
        func.count(
            TransactionTable.transaction_id
        )
    ).filter(
        TransactionTable.store_id == store_id
    ).scalar() or 0

    avg_dwell = db.query(
        func.avg(
            EventTable.dwell_ms
        )
    ).filter(
        EventTable.store_id == store_id
    ).scalar() or 0

    billing_queue = db.query(
        func.count(
            EventTable.event_id
        )
    ).filter(
        EventTable.store_id == store_id,
        EventTable.event_type ==
        "BILLING_QUEUE_JOIN"
    ).scalar() or 0

    conversion = (
        transactions /
        max(visitors, 1)
    ) * 100

    if avg_dwell > 10000:

        anomalies.append({

            "type":
            "HIGH_DWELL",

            "severity":
            "MEDIUM",

            "message":
            "Customers spending unusually long time in store",

            "value":
            int(avg_dwell)
        })

    if visitors < 10:

        anomalies.append({

            "type":
            "LOW_TRAFFIC",

            "severity":
            "HIGH",

            "message":
            "Store traffic below expected",

            "value":
            visitors
        })

    if conversion < 20:

        anomalies.append({

            "type":
            "LOW_CONVERSION",

            "severity":
            "HIGH",

            "message":
            "Many visitors but few purchases",

            "value":
            round(conversion, 2)
        })

    if billing_queue > 15:

        anomalies.append({

            "type":
            "QUEUE_CONGESTION",

            "severity":
            "MEDIUM",

            "message":
            "Billing queue unusually crowded",

            "value":
            billing_queue
        })

    return anomalies


def get_anomalies(
    db,
    store_id
):
    return detect_anomalies(
        db,
        store_id
    )