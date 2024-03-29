from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/hi')
def index():
    return 'Hello, World with waitress!!!'

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=50100, threads=1, url_prefix="/my-app")
