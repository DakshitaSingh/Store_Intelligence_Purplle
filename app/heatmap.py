import json

from app.schema import EventTable


def get_heatmap(
    db,
    store_id
):

    events = (
        db.query(EventTable)
        .filter(
            EventTable.store_id == store_id
        )
        .all()
    )

    zones = {}

    for e in events:

        if not e.zone_id:
            continue

        if e.zone_id not in zones:

            zones[e.zone_id] = {
                "visits": 0,
                "dwell": 0
            }

        zones[e.zone_id]["visits"] += 1

        if e.dwell_ms:
            zones[e.zone_id]["dwell"] += e.dwell_ms

    result = []

    max_visits = max(
        [v["visits"] for v in zones.values()],
        default=1
    )

    for zone, data in zones.items():

        score = int(
            (data["visits"] / max_visits)
            * 100
        )

        result.append(
            {
                "zone": zone,
                "visit_count": data["visits"],
                "avg_dwell_ms": data["dwell"],
                "heat_score": score,
                "data_confidence":
                    "LOW"
                    if data["visits"] < 20
                    else "HIGH"
            }
        )

    return result