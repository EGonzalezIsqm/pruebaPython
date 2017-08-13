CREATE TABLE factura (
  numeroFactura int(11) NOT NULL,
  fechaEmision varchar(45) NOT NULL,
  fechaRadicacion varchar(45) NOT NULL,
  fechaVencimiento varchar(45) NOT NULL,
  fechaPago varchar(45) NOT NULL,
  valorBruto varchar(45) NOT NULL,
  descuento varchar(45) DEFAULT NULL,
  iva varchar(45) NOT NULL,
  retencionIva varchar(45) NOT NULL,
  retencionFuente varchar(45) NOT NULL,
  retencionICA varchar(45) DEFAULT NULL,
  otrasRetenciones varchar(45) DEFAULT NULL
);
