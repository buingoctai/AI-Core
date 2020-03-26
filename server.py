from flask import Flask, jsonify,request
import os
import json
from evaluate import writeInputedUser
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/userData_classification', methods=['POST'])
def userData_classification():

    data=request.get_json()
    writeInputedUser(data['userName'])
    with open('predictiveMessage.json', 'r') as f:
        res = json.load(f)
        response = res
    return response


if __name__ == '__main__':
    app.run()
