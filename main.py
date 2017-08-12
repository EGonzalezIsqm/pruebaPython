from flask import Flask, render_template, request, url_for, redirect,jsonify,json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://python:prueba12345@localhost/dbpython'

db = SQLAlchemy(app)


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


class Prueba(db.Model):
    __tablename__ = 'prueba'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


db.create_all()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/registrofacturas')
def factura():
    return render_template('factura.html')


@app.route('/registroprueba')
def prueba():
    return render_template('formulario.html')


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


@app.route('/lista')
def lista():
    factura = Factura.query.all()
    return render_template("lista.html", factura=factura)


@app.route('/json' , methods=['GET'])
def listaJson():
    colum = ['numeroFactura', 'fechaEmision', 'fechaRadicacion','fechaVencimiento','fechaPago','valorBruto','descuento','iva',      'retencionIva','retencionFuente','retencionICA','otrasRetenciones']
    data = Factura.query.all()
    factura = [{col: getattr(d, col) for col in colum} for d in data]
    return jsonify(Factura=factura)


@app.route('/json/<int:id>/' , methods=['GET'])
def get_dev(id):
    colum = ['numeroFactura', 'fechaEmision', 'fechaRadicacion', 'fechaVencimiento', 'fechaPago', 'valorBruto',
             'descuento', 'iva', 'retencionIva', 'retencionFuente', 'retencionICA', 'otrasRetenciones']
    data = Factura.query.filter_by(numeroFactura=id).first()
    factura = [{col: getattr(d, col) for col in colum} for d in data]
    return jsonify(factura=factura)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    factura = Factura.query.filter_by(numeroFactura=id).first()

    db.session.delete(factura)
    db.session.commit()

    factura = factura.query.all()

    return render_template('lista.html', factura=factura)


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


if __name__ == '__main__':
    app.run(port=8000)
