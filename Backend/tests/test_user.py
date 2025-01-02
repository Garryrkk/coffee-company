def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}

def test_user_signup(client):
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "strongpassword"
    }
    response = client.post("/api/v1/users/signup", json=payload)
    assert response.status_code == 201
    assert "message" in response.json()
