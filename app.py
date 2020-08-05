#!/usr/bin/env python

import math
import json
import random 
from flask import (Flask, jsonify, request, abort, render_template, logging, Blueprint)
from flask_cors import CORS 
from calculator import Calculator

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)
PrometheusMetrics(app)


@app.route('/')
def main():
    return 'OK'

@app.route('/add', methods=['POST'])
def add_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.add(arg1, arg2)
        app.logger.info('{ "operation": "add", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/subtract', methods=['POST'])
def subtract_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.subtract(arg1, arg2)
        app.logger.info('{ "operation": "subtract", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/multiply', methods=['POST'])
def multiply_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.multiply(arg1, arg2)
        app.logger.info('{ "operation": "multiply", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/division', methods=['POST'])
def division_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.division(arg1, arg2)
        app.logger.info('{ "operation": "division", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        abort(400)

@app.route('/random')
def random_a(id=10):
    list = random.sample(range(1, 1000), id) 
    return ' '.join([str(elem) for elem in list]) 

@app.route('/random/<int:id>')
def random_args(id=10):
    list = random.sample(range(1, 1000), id) 
    return ' '.join([str(elem) for elem in list]) 

@app.route('/readiness')
def readiness():
    return {'message': 'readiness'}

@app.route('/liveness')
def liveness():
    return {'message': 'liveness'}

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
