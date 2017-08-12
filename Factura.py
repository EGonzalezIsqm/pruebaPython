from Persistencia import db

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
