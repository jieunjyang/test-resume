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
    if response.status_code != 500:
        logger.error('%s %s %s %s %s', request.remote_addr, request.method,
        request.scheme, request.full_path, request.status)
    return "OK"


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    app.run()
