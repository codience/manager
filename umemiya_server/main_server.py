# coding: utf-8
import os
import sys

from funcs import meta_func as meta
from funcs import common_func as common

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
config = meta.read_yaml('config.yml')
apis = meta.read_api_path('.api_path')
host = '0.0.0.0' if config['public'] == True else ''
port = int(config['port'])

@app.route('/')
def index():
    notice = meta.home()
    return notice

@app.route(apis['base'] + apis['transfer'])
def exec_transfer():
    return render_template('transfer.html')


@app.route(apis['adminonly'] + apis['print'])
def print_lesson():
    return render_template('print.html')

@app.route(apis['adminonly'] + apis['insert'], methods=["GET", "POST"])
def add_user():
    try:
        value_list = request.form.getlist('user_status')
        # return ["名前", "カナ","性別"]
        common.add_csv(value_list)
    except:
        value_list = []
    return render_template('add_user.html', value_list=value_list)


if __name__ == '__main__':
    app.run(debug=True)