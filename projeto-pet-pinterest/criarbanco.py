
from peterest import database, app
from peterest.models import Usuario, Foto

with app.app_context():
    database.create_all()