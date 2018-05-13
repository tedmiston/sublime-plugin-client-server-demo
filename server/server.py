import sys

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        'hello': 'world',
        'version': sys.version,
    })

@app.route('/upper', methods=['POST'])
def upper():
    text = request.json['text']
    return jsonify({
        'input': text,
        'output': text.upper(),
    })
