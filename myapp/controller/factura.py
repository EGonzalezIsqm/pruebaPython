# vim:fileencoding=utf8
from flask import render_template, redirect, url_for, request, Flask
from myapp.model.factura import FacturaModel

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')




