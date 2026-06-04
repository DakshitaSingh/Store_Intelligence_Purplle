from app.schema import EventTable


def build_funnel(
    db,
    store_id
):

    events = (
        db.query(EventTable)
        .filter(
            EventTable.store_id == store_id,
            EventTable.is_staff == False
        )
        .all()
    )

    visitors = {}

    for e in events:

        if e.visitor_id not in visitors:
            visitors[e.visitor_id] = {
                "entry": False,
                "zone": False,
                "billing": False
            }

        if e.event_type == "ENTRY":
            visitors[e.visitor_id]["entry"] = True

        if e.event_type == "ZONE_ENTER":
            visitors[e.visitor_id]["zone"] = True

        if (
            e.event_type ==
            "BILLING_QUEUE_JOIN"
        ):
            visitors[e.visitor_id]["billing"] = True

    entry = sum(
        1
        for v in visitors.values()
        if v["entry"]
    )

    zone = sum(
        1
        for v in visitors.values()
        if v["zone"]
    )

    billing = sum(
        1
        for v in visitors.values()
        if v["billing"]
    )

    return {
        "entry": entry,
        "zone_visit": zone,
        "billing": billing
    }