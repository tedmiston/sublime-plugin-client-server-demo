import sys

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/upper', methods=['POST'])
def upper():
    text = request.json['text']
    return jsonify({
        'input': text,
        'output': text.upper(),
    })

@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        'version': sys.version,
    })
