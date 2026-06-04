import os
import pandas as pd

from sqlalchemy.orm import Session
from app.schema import TransactionTable


def load_transactions(
    db: Session,
    csv_path="data/pos/transactions.csv"
):

    if not os.path.exists(csv_path):
        print(f"POS file not found: {csv_path}")
        return

    existing = (
        db.query(TransactionTable)
        .first()
    )

    if existing:
        return

    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():

        timestamp = (
            str(row["order_date"])
            + " "
            + str(row["order_time"])
        )

        txn = TransactionTable(
            transaction_id=str(
                row["order_id"]
            ),
            store_id=str(
                row["store_id"]
            ),
            timestamp=timestamp,
            basket_value=float(
                row["total_amount"]
            )
        )

        db.add(txn)

    db.commit()

    print(
        f"Loaded {len(df)} transactions"
    )