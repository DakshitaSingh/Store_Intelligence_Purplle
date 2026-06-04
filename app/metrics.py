from sqlalchemy import func

from app.schema import (
    EventTable,
    TransactionTable
)


def get_store_metrics(
    db,
    store_id
):

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
    ).scalar()

    avg_dwell = int(
        avg_dwell or 0
    )

    conversion_rate = min(
        round(
            (
                transactions /
                max(visitors, 1)
            ) * 100,
            2
        ),
        100
    )

    return {
        "unique_visitors": visitors,
        "transactions": transactions,
        "conversion_rate": conversion_rate,
        "avg_dwell_ms": avg_dwell
    }