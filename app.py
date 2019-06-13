import os
import logging
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    try:
        return "OK"
    except Exception as e:
        app.logger.error(e)
        return e

@app.route("/api/v1/test", methods=['GET'])
def get_test():
    app.logger.info('Test log2')
    print('print statement')
    app.logger.error('An error occured')
    app.logger.warning('A warning occured')
    return "Test."

if __name__ == '__main__':
    app.run()
