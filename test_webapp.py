from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# need to run in CMD: set FLASK_APP=test_webapp.py
# then run: python -m flask run
