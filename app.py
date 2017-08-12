import csv
import MySQLdb
import itertools

mydb = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='',
                       db='dbpython')
cursor = mydb.cursor()

csv_data = csv.reader(file('./static/facturas.csv'))
a=[]
i=0
k=0
for i in range(0,200):
    for row in itertools.islice(csv_data, k, k+100):
        a.append(row)
        print row
        print k
    print k



    sql="INSERT INTO factura (numeroFactura,fechaEmision,fechaRadicacion,fechaVencimiento,fechaPago,valorBruto," \
        "descuento,iva,retencionIva,retencionFuente,retencionICA,otrasRetenciones ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s," \
        "%s,%s,%s,%s)".format(str)
    number_of_rows = cursor.executemany(sql, a)
    a=[]
    mydb.commit()
cursor.close()
print "Done"
