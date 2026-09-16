VALID_PAYLOAD = {
    "carpet_area_sqft": 1200,
    "floor_num": 5,
    "Bathroom": 2,
    "Balcony": 1,
    "location_grouped": "mumbai",
    "Furnishing": "Semi-Furnished",
    "Transaction": "Resale",
    "Ownership": "Freehold",
    "facing": "East",
}


def test_predict_happy_path(client):
    response = client.post("/predict", json=VALID_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    assert body["predicted_price"] > 0
    assert body["predicted_price_lac"] > 0
    assert body["predicted_price_cr"] > 0
    assert body["currency"] == "INR"


def test_predict_invalid_input(client):
    payload = {**VALID_PAYLOAD, "carpet_area_sqft": -100}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_predict_unknown_location(client):
    payload = {**VALID_PAYLOAD, "location_grouped": "not-a-real-city"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["predicted_price"] > 0
