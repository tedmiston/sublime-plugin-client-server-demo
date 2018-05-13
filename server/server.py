import subprocess
import sys

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/bash', methods=['POST'])
def bash():
    command = request.json['command']

    proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True,
                          universal_newlines=True)
    output = proc.stdout

    return jsonify({
        'command': command,
        'output': output,
    })


@app.route('/upper', methods=['GET'])
def upper():
    text = request.args['text']
    output = text.upper()

    return jsonify({
        'input': text,
        'output': output,
    })


@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        'version': sys.version,
    })
