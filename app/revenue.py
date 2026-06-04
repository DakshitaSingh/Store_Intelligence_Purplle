from sqlalchemy import func

from app.schema import (
    TransactionTable
)


def revenue_metrics(
    db,
    store_id
):

    revenue = db.query(
        func.sum(
            TransactionTable
            .basket_value
        )
    ).filter(
        TransactionTable.store_id
        == store_id
    ).scalar() or 0

    avg_basket = db.query(
        func.avg(
            TransactionTable
            .basket_value
        )
    ).filter(
        TransactionTable.store_id
        == store_id
    ).scalar() or 0

    return {

        "total_revenue":
        round(
            revenue,
            2
        ),

        "avg_basket":
        round(
            avg_basket,
            2
        )
    }