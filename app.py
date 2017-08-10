from flask import Flask,render_template,request,url_for,redirect
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLACHEMY_DATABASE_URI'] = 'mysql+pymqsl://user:root@localhost/dbpython'

db = SQLAlchemy(app)

class Factura(db.Model):
    __tablename__='factura'

    numeroFactura=db.Column(db.Integer,primary_key=True)
    fechaEmision=db.Column(db.String(45))
    fechaRadicacion=db.Column(db.String(45))
    fechaVencimiento=db.Column(db.String(45))
    fechaPago=db.Column(db.String(45))
    valorBruto=db.Column(db.Integer)
    descuento=db.Column(db.Integer)
    iva=db.Column(db.Integer)
    retencionIva=db.Column(db.Integer)
    retencionFuente=db.Column(db.Integer)
    retencionICA=db.Column(db.Integer)
    otrasRetenciones=db.Column(db.Integer)

    def __init__(self,fechaEmision,fechaRadicacion,fechaVencimiento,fechaPago,valorBruto,descuento,iva,retencionIva,retencionFuente,
                 retencionICA,otrasRetenciones):
        self.fechaEmision = fechaEmision
        self.fechaRadicacion=fechaRadicacion
        self.fechaVencimiento=fechaVencimiento
        self.fechaPago=fechaPago
        self.valorBruto=valorBruto
        self.descuento=descuento
        self.iva=iva
        self.retencionIva=retencionIva
        self.retencionFuente=retencionFuente
        self.retencionICA=retencionICA
        self.otrasRetenciones=otrasRetenciones

    db.create_all()

@app.route("/")
@app.route("/index")
def index():
    return  "<h1>Funciona</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)