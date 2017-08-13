from myapp import db
from myapp.db.orm.factura import Factura
    
    
class FacturaModel(object):
        def get_entries(self):
            return db.session.query(Factura).all()
    
        def save(self, numeroFactura, fechaEmision, fechaRadicacion, fechaVencimiento, fechaPago, valorBruto,
                 descuento, iva, retencionIva, retencionFuente, retencionICA, otrasRetenciones):
            db.session.add(Factura(numeroFactura, fechaEmision, fechaRadicacion, fechaVencimiento, fechaPago, valorBruto,
                 descuento, iva, retencionIva, retencionFuente, retencionICA, otrasRetenciones))
            db.session.commit()