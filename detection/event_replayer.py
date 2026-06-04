import json
import time
import requests


API_URL = (
    "http://127.0.0.1:8000"
    "/events/ingest"
)

EVENT_FILE = (
    "../data/generated_events/"
    "store1_events.jsonl"
)


def replay_events():

    batch = []

    with open(
        EVENT_FILE,
        "r"
    ) as f:

        for line in f:

            event = json.loads(
                line
            )

            batch.append(
                event
            )

            if len(batch) == 20:

                response = requests.post(
                    API_URL,
                    json=batch
                )

                print(
                    response.json()
                )

                batch = []

                time.sleep(1)

    if batch:

        response = requests.post(
            API_URL,
            json=batch
        )

        print(
            response.json()
        )


if __name__ == "__main__":

    replay_events()