from app.schema import EventTable
from app.schema import TransactionTable


def get_health(db):

    event_count = (
        db.query(EventTable)
        .count()
    )

    transaction_count = (
        db.query(TransactionTable)
        .count()
    )

    latest = (
        db.query(EventTable)
        .order_by(
            EventTable.timestamp.desc()
        )
        .first()
    )

    return {

        "status": "healthy",

        "events_ingested":
        event_count,

        "transactions_loaded":
        transaction_count,

        "last_event":
        latest.timestamp
        if latest else None
    }