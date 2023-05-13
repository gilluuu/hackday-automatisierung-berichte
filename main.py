#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
import subprocess
import Code.getBEData as bedata

app = Flask(__name__,
            static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    return render_template('message.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
