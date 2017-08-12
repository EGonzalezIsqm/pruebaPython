import csv

from flask import Flask, render_template, request, url_for, redirect, jsonify, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# Conexion ala Base de Datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://python:prueba12345@localhost/dbpython'

db = SQLAlchemy(app)


# Modelo Factura que hace referencia a nuestra tabla de la db
class Factura(db.Model):
    __tablename__ = 'factura'

    numeroFactura = db.Column(db.Integer, primary_key=True)
    fechaEmision = db.Column(db.String(45))
    fechaRadicacion = db.Column(db.String(45))
    fechaVencimiento = db.Column(db.String(45))
    fechaPago = db.Column(db.String(45))
    valorBruto = db.Column(db.String(45))
    descuento = db.Column(db.String(45))
    iva = db.Column(db.String(45))
    retencionIva = db.Column(db.String(45))
    retencionFuente = db.Column(db.String(45))
    retencionICA = db.Column(db.String(45))
    otrasRetenciones = db.Column(db.String(45))

    def __init__(self, numeroFactura, fechaEmision, fechaRadicacion, fechaVencimiento, fechaPago, valorBruto, descuento,
                 iva, retencionIva, retencionFuente,
                 retencionICA, otrasRetenciones):
        self.numeroFactura = numeroFactura
        self.fechaEmision = fechaEmision
        self.fechaRadicacion = fechaRadicacion
        self.fechaVencimiento = fechaVencimiento
        self.fechaPago = fechaPago
        self.valorBruto = valorBruto
        self.descuento = descuento
        self.iva = iva
        self.retencionIva = retencionIva
        self.retencionFuente = retencionFuente
        self.retencionICA = retencionICA
        self.otrasRetenciones = otrasRetenciones


# Modelo refenrente a tabla de prueba de la db
class Prueba(db.Model):
    __tablename__ = 'prueba'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


db.create_all()

"""
Metodo que renderiza el index
"""


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


"""
Metodo que renderiza el formulario
de registro de facturas
"""


@app.route('/registrofacturas')
def factura():
    return render_template('factura.html')


"""
Metodo que renderiza el formulario
de prueba
"""


@app.route('/registroprueba')
def prueba():
    return render_template('formulario.html')


"""
Metodo que ejecuta la accion de 
almacenar una prueba
"""


@app.route('/formulario', methods=['GET', 'POST'])
def registroPrueba():
    if request.method == 'POST':
        id = request.form.get("id")
        nombre = request.form.get("nombre")
    if id and nombre:
        p = Prueba(id, nombre)
        db.session.add(p)
        db.session.commit()

    return redirect(url_for('index'))


"""
Metodo que hace la accion de registrar
una nueva factura
"""


@app.route('/factura', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        numeroFactura = request.form.get("numeroFactura")
        fechaEmision = request.form.get("fechaEmision")
        fechaRadicacion = request.form.get("fechaRadicacion")
        fechaVencimiento = request.form.get("fechaVencimiento")
        fechaPago = request.form.get("fechaPago")
        valorBruto = request.form.get("valorBruto")
        descuento = request.form.get("descuento")
        iva = request.form.get("iva")
        retencionIva = request.form.get("retencionIva")
        retencionFuente = request.form.get("retencionFuente")
        retencionICA = request.form.get("retencionICA")
        otrasRetenciones = request.form.get("otrasRetenciones")

    if numeroFactura and fechaEmision and fechaRadicacion and fechaVencimiento and fechaPago and valorBruto and descuento and iva and retencionIva and retencionFuente and retencionICA and otrasRetenciones:
        f = Factura(numeroFactura, fechaEmision, fechaRadicacion, fechaVencimiento, fechaPago, valorBruto, descuento,
                    iva, retencionIva,
                    retencionFuente, retencionICA, otrasRetenciones)
        db.session.add(f)
        db.session.commit()

    return redirect(url_for("index"))


"""
Metodo que consulta todos 
las facturas existentes
"""


@app.route('/lista')
def lista():
    factura = Factura.query.all()
    return render_template("lista.html", factura=factura)


"""
Metodo que me retorna un archivo
en formato JSON con todas las 
facturas existentes 
"""


@app.route('/json', methods=['GET'])
def listaJson():
    colum = ['numeroFactura', 'fechaEmision', 'fechaRadicacion', 'fechaVencimiento', 'fechaPago', 'valorBruto',
             'descuento', 'iva', 'retencionIva', 'retencionFuente', 'retencionICA', 'otrasRetenciones']
    data = Factura.query.all()
    factura = [{col: getattr(d, col) for col in colum} for d in data]
    return jsonify(Factura=factura)


"""
Metodo que me retorna un archivo
en formato JSON con una unica 
factura,la consulta se hace por
medio del numero de factura
"""


@app.route('/json/<int:id>/', methods=['GET'])
def get_dev(id):
    colum = ['numeroFactura', 'fechaEmision', 'fechaRadicacion', 'fechaVencimiento', 'fechaPago', 'valorBruto',
             'descuento', 'iva', 'retencionIva', 'retencionFuente', 'retencionICA', 'otrasRetenciones']
    data = Factura.query.filter_by(numeroFactura=id).first()
    factura = [{col: getattr(d, col) for col in colum} for d in data]
    return jsonify(factura=factura)


"""
Metodo que elimina una factura
"""


@app.route('/eliminar/<int:id>')
def eliminar(id):
    factura = Factura.query.filter_by(numeroFactura=id).first()

    db.session.delete(factura)
    db.session.commit()

    factura = factura.query.all()

    return render_template('lista.html', factura=factura)


"""
Metodo que edita una factura 
"""


@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar(id):
    factura = Factura.query.filter_by(numeroFactura=id).first()
    if request.method == 'POST':
        fechaEmision = request.form.get("fechaEmision")
        fechaRadicacion = request.form.get("fechaRadicacion")
        fechaVencimiento = request.form.get("fechaVencimiento")
        fechaPago = request.form.get("fechaPago")
        valorBruto = request.form.get("valorBruto")
        descuento = request.form.get("descuento")
        iva = request.form.get("iva")
        retencionIva = request.form.get("retencionIva")
        retencionFuente = request.form.get("retencionFuente")
        retencionICA = request.form.get("retencionICA")
        otrasRetenciones = request.form.get("otrasRetenciones")

        if fechaEmision and fechaRadicacion and fechaVencimiento and fechaPago and valorBruto and descuento and iva and retencionIva and retencionFuente and retencionICA and otrasRetenciones:
            factura.fechaEmision = fechaEmision
            factura.fechaRadicacion = fechaRadicacion
            factura.fechaVencimiento = fechaVencimiento
            factura.fechaPago = fechaPago
            factura.valorBruto = valorBruto
            factura.descuento = descuento
            factura.iva = iva
            factura.retencionIva = retencionIva
            factura.retencionFuente = retencionFuente
            factura.retencionICA = retencionICA
            factura.otrasRetenciones = otrasRetenciones

            db.session.commit()

        return redirect(url_for('lista'))

    return render_template('actualizar.html', factura=factura)


"""
Metodo que sube un csv y muestra
sus datos en formato json 
"""
csv_path = './static/facturas.csv'
csv_obj = csv.DictReader(open(csv_path, 'r'))
csv_list = list(csv_obj)


@app.route('/cargarCSV')
def cargarCSV():
    return render_template('archivo.html', object_list=csv_list)


"""
Metodo que sube nuestra 
app
"""
if __name__ == '__main__':
    app.run(port=8000)
