# Activar el entorno virtual venv_flask
venv_flask\Scripts\activate

# Configurar la variable de entorno FLASK_APP
$env:FLASK_APP = "app.py"

# Abriendo la app en el navegador
Start-Process "init.bat" -WindowStyle Hidden


# Ejecutar flask run directamente desde el directorio de la aplicación
flask run
# Servidor listo