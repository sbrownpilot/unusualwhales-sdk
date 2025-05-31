import requests

def authenticate(username: str, password: str) -> requests.Session:
    session = requests.Session()
    response = session.post("https://api.unusualwhales.com/auth", json={
        "username": username,
        "password": password
    })
    response.raise_for_status()
    token = response.json()["token"]
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

