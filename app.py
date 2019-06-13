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


@app.after_request
def after_request(response):
    try:
        if response.status_code != 500:
            app.logger.error('%s %s %s %s %s', request.remote_addr, request.method,
            request.scheme, request.full_path, request.status)

            return response
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run()
