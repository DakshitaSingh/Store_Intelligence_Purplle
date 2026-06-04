import uuid


def create_event(
    store_id,
    camera_id,
    visitor_id,
    event_type,
    timestamp,
    zone_id=None,
    confidence=0.90,
    dwell_ms=0,
    metadata=None
):

    if metadata is None:
        metadata = {}

    return {

        "event_id":
        str(uuid.uuid4()),

        "store_id":
        store_id,

        "camera_id":
        camera_id,

        "visitor_id":
        visitor_id,

        "event_type":
        event_type,

        "timestamp":
        timestamp,

        "zone_id":
        zone_id,

        "dwell_ms":
        dwell_ms,

        "is_staff":
        False,

        "confidence":
        confidence,

        "metadata":
        metadata
    }