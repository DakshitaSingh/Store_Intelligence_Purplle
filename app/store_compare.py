from app.metrics import (
    get_store_metrics
)


def compare_stores(
    db,
    store_ids
):

    output = []

    for store_id in store_ids:

        metrics = get_store_metrics(
            db,
            store_id
        )

        output.append({

            "store_id":
            store_id,

            **metrics
        })

    return output