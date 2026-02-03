import requests
import time

for _ in range(10):
    try:
        r = requests.get("http://localhost:8081/api/ping")
        break
    except requests.exceptions.ConnectionError:
        time.sleep(2)
else:
    raise Exception("No se pudo conectar al servicio NGINX/Gunicorn")

def test_ping():
    assert r.status_code == 200
    assert r.json() == {"response": "pong"}
