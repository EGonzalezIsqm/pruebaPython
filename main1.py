from flask import Flask

# Flask App
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)