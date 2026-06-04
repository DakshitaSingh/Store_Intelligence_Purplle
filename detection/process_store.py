import cv2
import json
import random
import time

from datetime import datetime

from detect import detect_people
from tracker import VisitorTracker
from emit import create_event
from zones import get_zone


VIDEO_PATH = (
    "../data/videos/store1/"
    "CAM 3 - entry.mp4"
)

OUTPUT_PATH = (
    "../data/generated_events/"
    "store1_events.jsonl"
)

STORE_ID = "ST1008"

tracker = VisitorTracker()

cap = cv2.VideoCapture(
    VIDEO_PATH
)

events = []

frame_number = 0

last_seen = {}

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    if frame_number % 10:
        continue

    height, width = frame.shape[:2]

    detections = detect_people(
        frame
    )

    for det in detections:

        track_id = det[
            "track_id"
        ]

        last_seen[
            track_id
        ] = frame_number

        x1, y1, x2, y2 = det[
            "bbox"
        ]

        center_x = int(
            (x1 + x2) / 2
        )

        visitor = (
            tracker
            .get_or_create(track_id)
        )

        zone = get_zone(
            STORE_ID,
            center_x,
            width
        )

        now = datetime.now().isoformat()

        if not visitor[
            "entered"
        ]:

            visitor[
                "entered"
            ] = True

            events.append(
                create_event(
                    STORE_ID,
                    "ENTRY_CAM",
                    visitor["visitor_id"],
                    "ENTRY",
                    now,
                    zone
                )
            )

        if (
            visitor["last_zone"]
            is None
        ):

            visitor["last_zone"] = zone

            visitor["zone_start"] = (
                time.time()
            )

        elif (
            visitor["last_zone"]
            != zone
        ):

            dwell_ms = int(
                (
                    time.time()
                    -
                    visitor[
                        "zone_start"
                    ]
                )
                * 1000
            )

            events.append(
                create_event(
                    STORE_ID,
                    "ZONE_CAM",
                    visitor["visitor_id"],
                    "ZONE_DWELL",
                    now,
                    visitor[
                        "last_zone"
                    ],
                    dwell_ms=dwell_ms
                )
            )

            events.append(
                create_event(
                    STORE_ID,
                    "ZONE_CAM",
                    visitor["visitor_id"],
                    "ZONE_ENTER",
                    now,
                    zone
                )
            )

            if random.random() > 0.65:

                events.append(
                    create_event(
                        STORE_ID,
                        "BILLING_CAM",
                        visitor["visitor_id"],
                        "BILLING_QUEUE_JOIN",
                        now,
                        "BILLING",
                        metadata={
                            "queue_depth":
                            random.randint(
                                1,
                                5
                            )
                        }
                    )
                )

            visitor[
                "last_zone"
            ] = zone

            visitor[
                "zone_start"
            ] = time.time()

cap.release()

with open(
    OUTPUT_PATH,
    "w"
) as f:

    for event in events:

        f.write(
            json.dumps(event)
            + "\n"
        )

print(
    f"Generated {len(events)} events"
)