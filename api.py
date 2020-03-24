from flask import Flask, jsonify
import os
import json
from evaluate import writeInputedUser
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/userData_classification', methods=['GET'])
def test_connect():
    writeInputedUser(['long time no meet'])
    with open('predictiveMessage.json', 'r') as f:
        res = json.load(f)
        response = res
    return response


if __name__ == '__main__':
    app.run()
