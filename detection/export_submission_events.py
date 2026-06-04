import json

INPUT_FILES = [
    "data/generated_events/store1_events.jsonl",
    "data/generated_events/multicam_events.jsonl"
]

OUTPUT_FILE = "data/generated_events/submission_events.jsonl"


def convert_event(event):
    event_type = event.get("event_type", "")

    if event_type == "ENTRY":
        return {
            "event_type": "entry",
            "id_token": event["visitor_id"],
            "store_code": event["store_id"],
            "camera_id": event["camera_id"],
            "event_timestamp": event["timestamp"],
            "is_staff": event.get("is_staff", False),
            "gender_pred": "Unknown",
            "age_pred": None,
            "age_bucket": None,
            "is_face_hidden": False,
            "group_id": None,
            "group_size": None
        }

    elif event_type == "EXIT":
        return {
            "event_type": "exit",
            "id_token": event["visitor_id"],
            "store_code": event["store_id"],
            "camera_id": event["camera_id"],
            "event_timestamp": event["timestamp"],
            "is_staff": event.get("is_staff", False),
            "gender_pred": "Unknown",
            "age_pred": None,
            "age_bucket": None,
            "is_face_hidden": False,
            "group_id": None,
            "group_size": None
        }

    elif event_type == "ZONE_ENTER":
        return {
            "event_type": "zone_entered",
            "track_id": event["visitor_id"],
            "store_id": event["store_id"],
            "camera_id": event["camera_id"],
            "zone_id": event["zone_id"],
            "zone_name": event["zone_id"],
            "zone_type": "SHELF",
            "is_revenue_zone": "Yes",
            "event_time": event["timestamp"],
            "zone_hotspot_x": 0,
            "zone_hotspot_y": 0,
            "gender": "Unknown",
            "age": None,
            "age_bucket": None
        }

    elif event_type == "ZONE_DWELL":
        return {
            "event_type": "zone_exited",
            "track_id": event["visitor_id"],
            "store_id": event["store_id"],
            "camera_id": event["camera_id"],
            "zone_id": event["zone_id"],
            "zone_name": event["zone_id"],
            "zone_type": "SHELF",
            "is_revenue_zone": "Yes",
            "event_time": event["timestamp"],
            "zone_hotspot_x": 0,
            "zone_hotspot_y": 0,
            "gender": "Unknown",
            "age": None,
            "age_bucket": None
        }

    elif event_type == "BILLING_QUEUE_JOIN":
        return {
            "queue_event_id": event["event_id"],
            "event_type": "queue_joined",
            "track_id": event["visitor_id"],
            "store_id": event["store_id"],
            "camera_id": event["camera_id"],
            "zone_id": event["zone_id"],
            "zone_name": "Billing Counter Queue",
            "zone_type": "BILLING",
            "is_revenue_zone": "Yes",
            "queue_join_ts": event["timestamp"],
            "queue_served_ts": None,
            "queue_exit_ts": None,
            "wait_seconds": 0,
            "queue_position_at_join": event.get(
                "metadata", {}
            ).get("queue_depth", 0),
            "abandoned": False,
            "zone_hotspot_x": 0,
            "zone_hotspot_y": 0,
            "gender": "Unknown",
            "age": None,
            "age_bucket": None
        }

    return None


with open(OUTPUT_FILE, "w") as outfile:

    for input_file in INPUT_FILES:

        with open(input_file, "r") as infile:

            for line in infile:

                event = json.loads(line)

                converted = convert_event(event)

                if converted:
                    outfile.write(
                        json.dumps(converted) + "\n"
                    )

print(f"Created {OUTPUT_FILE}")