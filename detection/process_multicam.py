import cv2
import json
import uuid

from datetime import datetime

OUTPUT_FILE = (
    "../data/generated_events/"
    "multicam_events.jsonl"
)

VIDEOS = [
    ("ENTRY_CAM_1", "../data/videos/store2/entry 1.mp4"),
    ("ENTRY_CAM_2", "../data/videos/store2/entry 2.mp4"),
    ("ZONE_CAM", "../data/videos/store2/zone.mp4"),
    ("BILLING_CAM", "../data/videos/store2/billing_area.mp4")
]

STORE_ID = "ST1008"

events = []


def add_event(
    camera,
    visitor,
    event_type,
    zone
):

    events.append(
        {
            "event_id": str(
                uuid.uuid4()
            ),
            "store_id": STORE_ID,
            "camera_id": camera,
            "visitor_id": visitor,
            "event_type": event_type,
            "timestamp": datetime.now().isoformat(),
            "zone_id": zone,
            "dwell_ms": 0,
            "is_staff": False,
            "confidence": 0.90,
            "metadata": {}
        }
    )


visitor_counter = 1

for camera, path in VIDEOS:

    cap = cv2.VideoCapture(path)

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 150:
            continue

        visitor_id = (
            f"VISITOR_"
            f"{visitor_counter}"
        )

        visitor_counter += 1

        if "ENTRY" in camera:

            add_event(
                camera,
                visitor_id,
                "ENTRY",
                "ENTRANCE"
            )

        elif "ZONE" in camera:

            add_event(
                camera,
                visitor_id,
                "ZONE_ENTER",
                "CENTER_ZONE"
            )

            add_event(
                camera,
                visitor_id,
                "ZONE_DWELL",
                "CENTER_ZONE"
            )

        elif "BILLING" in camera:

            add_event(
                camera,
                visitor_id,
                "BILLING_QUEUE_JOIN",
                "RIGHT_ZONE"
            )

    cap.release()

with open(
    OUTPUT_FILE,
    "w"
) as f:

    for event in events:

        f.write(
            json.dumps(event)
            + "\n"
        )

print(
    f"Generated "
    f"{len(events)} events"
)