#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    output = subprocess.check_output(['python', 'code/pdfgeneration.py'])
    return output

if __name__ == '__main__':
    app.run()
