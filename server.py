from flask import Flask, jsonify, request
import os
import json
from evaluate import writeInputedUser
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/userData_classification', methods=['POST'])
def userData_classification():
    data = request.get_json()
    response={}
    i=0
    for item in data["list"]:
        writeInputedUser(item["data"],item["fileName"])
        with open(item["fileName"]+'.json', 'r') as f:
            response['response_'+str(i)] = json.load(f)
            i=i+1
    return response


if __name__ == '__main__':
    app.run()
