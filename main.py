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
    import Code.getBEData as bedata
    df = bedata.getChart1()
    print(df) 
    return 'Skript beendet'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
