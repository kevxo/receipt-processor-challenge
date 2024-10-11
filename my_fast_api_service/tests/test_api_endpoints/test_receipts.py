from tests.test_config import client


def test_create_receipt_process():
    payload = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2024-10-08",
        "purchaseTime": "13:01",
        "items": [{"shortDescription": "Grocery Store Visit", "price": "12.99"}],
        "total": "6.49",
    }

    response = client.post("/api/v1/receipts/process", json=payload)

    assert response.status_code == 201
    assert response.json()["id"]


def test_create_receipt_error():
    payload = {
        "purchaseDate": "2024-10-08",
        "purchaseTime": "13:01",
        "items": [{"shortDescription": "Grocery Store Visit", "price": "12.99"}],
        "total": "6.49",
    }

    response = client.post("/api/v1/receipts/process", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"]
