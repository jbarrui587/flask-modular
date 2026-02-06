# Práctica 12 – Flask modular con Docker y NGINX

## Descripción
En esta práctica se ha desarrollado una aplicación Flask modular utilizando Blueprints.  
La aplicación incluye una pequeña API REST, logging de peticiones, tests automáticos y un despliegue completo con Docker, Gunicorn y NGINX.

---

## Estructura del proyecto

app/
├── init.py
├── routes.py
├── api/
│ ├── init.py
│ └── endpoints.py
tests/
├── test_api.py
scripts/
├── test_api.sh
docker/
├── nginx_app.conf
logs/
├── app.log
Dockerfile
docker-compose.yml
wsgi.py
requirements.txt


---

## Cómo ejecutar el proyecto

Desde la raíz del proyecto ejecutar:


docker compose up --build
La aplicación estará disponible en:

http://localhost:8081

http://localhost:8081/info

http://localhost:8081/api/ping

http://localhost:8081/api/status

http://localhost:8081/api/items

## Tests con Pytest
Para ejecutar los tests:

pytest tests/test_api.py
El test comprueba que el endpoint /api/ping responde correctamente.

## Script de prueba
Ejecutar:

bash scripts/test_api.sh
Este script realiza peticiones a la API usando curl.

## Logs
Las peticiones HTTP se registran en el archivo:

logs/app.log

---

