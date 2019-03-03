import os
import sys

from funcs import meta_func as meta
from funcs import common_func as common

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
config = meta.read_yaml('config.yml')
host = '0.0.0.0' if config['public'] == True else ''
port = int(config['port'])

@app.route('/')
def index():
    notice = meta.home()
    return notice

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)