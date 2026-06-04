import requests


BASE = "http://127.0.0.1:8000"


def test_health():

    r = requests.get(
        f"{BASE}/health"
    )

    assert r.status_code == 200


def test_metrics():

    r = requests.get(
        f"{BASE}/stores/ST1008/metrics"
    )

    assert r.status_code == 200