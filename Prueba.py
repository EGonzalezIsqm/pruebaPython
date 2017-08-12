from Persistencia import db


class Prueba(db.Model):
    __tablename__ = 'prueba'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre