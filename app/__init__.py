from app.rutas.front import front

from app.app import app

app.register_blueprint(front)
