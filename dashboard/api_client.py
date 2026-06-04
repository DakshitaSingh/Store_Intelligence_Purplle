import requests
import os
BASE_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)


def get_metrics(store_id):

    r = requests.get(
        f"{BASE_URL}/stores/{store_id}/metrics"
    )

    return r.json()


def get_funnel(store_id):

    r = requests.get(
        f"{BASE_URL}/stores/{store_id}/funnel"
    )

    return r.json()


def get_heatmap(store_id):

    r = requests.get(
        f"{BASE_URL}/stores/{store_id}/heatmap"
    )

    return r.json()


def get_anomalies(store_id):

    r = requests.get(
        f"{BASE_URL}/stores/{store_id}/anomalies"
    )

    return r.json()

def get_revenue(
    store_id
):

    return requests.get(
        f"{BASE_URL}/stores/"
        f"{store_id}/revenue"
    ).json()


def get_queue(
    store_id
):

    return requests.get(
        f"{BASE_URL}/stores/"
        f"{store_id}/queue"
    ).json()
def get_health():

    r = requests.get(
        f"{BASE_URL}/health"
    )

    return r.json()