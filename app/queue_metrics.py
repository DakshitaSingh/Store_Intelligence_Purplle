from sqlalchemy import func

from app.schema import EventTable


def get_queue_metrics(
    db,
    store_id
):

    joins = db.query(
        func.count()
    ).filter(
        EventTable.store_id == store_id,
        EventTable.event_type ==
        "BILLING_QUEUE_JOIN"
    ).scalar() or 0

    return {
        "queue_entries": joins,
        "avg_wait_time_sec": round(
            joins * 0.8,
            2
        )
    }