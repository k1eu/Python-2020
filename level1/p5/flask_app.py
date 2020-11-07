from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/data')
def data():
    return {"name": "Xi", "age": 12}


@app.route('/calc')
def calc():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return {"suma": a + b}


if __name__ == '__main__':
    app.run()