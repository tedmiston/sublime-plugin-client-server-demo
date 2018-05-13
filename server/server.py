import sys

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def foo():
    return jsonify({
        'hello': 'world',
        'version': sys.version,
    })
