import subprocess
import sys

from flask import Flask, request

from utils import JsonResponse

app = Flask(__name__)
app.response_class = JsonResponse


@app.route('/bash', methods=['POST'])
def bash():
    command = request.json['command']

    proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True,
                          universal_newlines=True)
    output = proc.stdout

    return {
        'command': command,
        'output': output,
    }


@app.route('/upper', methods=['GET'])
def upper():
    text = request.args['text']
    output = text.upper()

    return {
        'input': text,
        'output': output,
    }


@app.route('/version', methods=['GET'])
def version():
    return {
        'version': sys.version,
    }
