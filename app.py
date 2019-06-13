import os
import logging
from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "OK"


@app.after_request
def after_request(response):
    if response.status_code != 500:
        app.logger.error('REQUEST URL: %s', request.url)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    app.logger.error('%s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
    request.remote_addr, request.method, request.scheme, request.full_path, tb)
    return 'bad request!'

if __name__ == '__main__':
    app.run()
