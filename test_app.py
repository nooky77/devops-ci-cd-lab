from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b'Bienvenue' in response.data


def test_groupe10():
    client = app.test_client()
    response = client.get("/groupe10")
    assert response.status_code == 200
    assert b'Groupe 10' in response.data


def test_groupe20():
    client = app.test_client()
    response = client.get("/groupe20")
    assert response.status_code == 200
    assert b'Groupe 20' in response.data


def test_groupe30():
    client = app.test_client()
    response = client.get("/groupe30")
    assert response.status_code == 200
    assert b'Groupe 30' in response.data


def test_groupe40():
    client = app.test_client()
    response = client.get("/groupe40")
    assert response.status_code == 200
    assert b'Groupe 40' in response.data


def test_groupe50():
    client = app.test_client()
    response = client.get("/groupe50")
    assert response.status_code == 200
    assert b'Groupe 50' in response.data
