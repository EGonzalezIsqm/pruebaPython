from myapp import db

class Factura(db.Model):
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


db.mapper(Factura,
          db.Table('factura', db.metadata, autoload=True))