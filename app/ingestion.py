import json

from sqlalchemy.orm import Session

from app.schema import EventTable


def ingest_events(
    db: Session,
    events
):
    accepted = 0
    duplicates = 0
    failed = 0

    for event in events:

        existing = db.get(
            EventTable,
            event.event_id
        )

        if existing:
            duplicates += 1
            continue

        try:

            row = EventTable(
                event_id=event.event_id,
                store_id=event.store_id,
                camera_id=event.camera_id,
                visitor_id=event.visitor_id,
                event_type=event.event_type,
                timestamp=event.timestamp,
                zone_id=event.zone_id,
                dwell_ms=event.dwell_ms,
                is_staff=event.is_staff,
                confidence=event.confidence,
                event_metadata=json.dumps(
                    event.metadata
                )
            )

            db.add(row)

            accepted += 1

        except Exception as e:
            print("INGEST ERROR:", e)
            failed += 1

    db.commit()

    return {
        "accepted": accepted,
        "duplicates": duplicates,
        "failed": failed
    }