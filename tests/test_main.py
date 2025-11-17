from app.main import app


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Github CI/CD Actions"


def test_info():
    response = app.test_client().get("/info")
    assert response.status_code == 200
    assert response.json["version"] == "1.0"


def test_page():
    response = app.test_client().get("/page")
    assert response.status_code == 200
    assert "CI/CD" in response.data.decode()
