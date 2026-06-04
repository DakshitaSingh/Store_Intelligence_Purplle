import json
import requests

API = (
    "http://127.0.0.1:8000/"
    "events/ingest"
)

FILE = (
    "../data/generated_events/"
    "multicam_events.jsonl"
)

batch = []

with open(FILE) as f:

    for line in f:

        batch.append(
            json.loads(line)
        )

        if len(batch) == 20:

            r = requests.post(
                API,
                json=batch
            )

            print(
                r.json()
            )

            batch = []

if batch:

    r = requests.post(
        API,
        json=batch
    )

    print(
        r.json()
    )