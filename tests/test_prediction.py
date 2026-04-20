def test_predict_valid(client):
    response = client.post(
        "/predictions/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        },
        headers={"X-API-KEY": "testsecretkey"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data 
    assert "predicted_class" in data


def test_predict_no_key(client):
    response = client.post(
        "/predictions/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )
    assert response.status_code == 401


def test_predict_wrong_key(client):
    response = client.post(
        "/predictions/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        },
        headers={"X-API-KEY": "wrongkey"}
    )
    assert response.status_code == 403


def test_get_predictions(client):
    response = client.get("/predictions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 