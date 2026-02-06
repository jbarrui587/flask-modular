# Comprobación – Práctica 12

## ¿Qué puerto usa Gunicorn?
Gunicorn usa el puerto 8000.

---

## ¿Qué hace el archivo nginx_app.conf?
Configura NGINX como proxy inverso para redirigir las peticiones a la aplicación Flask.

---

## ¿Dónde se escriben los logs?
Los logs se escriben en el archivo `logs/app.log`.

---

## ¿Para qué sirve wsgi.py?
Sirve como punto de entrada para que Gunicorn pueda ejecutar la aplicación Flask.
