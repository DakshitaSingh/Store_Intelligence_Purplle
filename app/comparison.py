from sqlalchemy import func

from app.schema import (
    EventTable,
    TransactionTable
)


def get_store_summary(
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
    ).scalar() or 0

    conversion = round(
        (
            transactions /
            max(visitors, 1)
        ) * 100,
        2
    )

    return {
        "store_id": store_id,
        "visitors": visitors,
        "transactions": transactions,
        "conversion": min(
            conversion,
            100
        ),
        "avg_dwell": int(
            avg_dwell
        )
    }


def compare_stores(
    db,
    store_a,
    store_b
):

    return {
        "store_a":
        get_store_summary(
            db,
            store_a
        ),

        "store_b":
        get_store_summary(
            db,
            store_b
        )
    }