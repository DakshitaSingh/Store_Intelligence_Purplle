from app.schema import EventTable


def get_journey(
    db,
    visitor_id
):

    rows = db.query(
        EventTable
    ).filter(
        EventTable.visitor_id
        ==
        visitor_id
    ).all()

    journey = []

    for row in rows:

        journey.append({
            "event_type":
            row.event_type,

            "zone":
            row.zone_id,

            "timestamp":
            row.timestamp
        })

    return journey