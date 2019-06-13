import os
import logging
from flask import Flask, request, jsonify
import traceback
from collections import defaultdict

options = defaultdict(lambda: "OK", {"Name": "Jinny Yang",
"Email Address": "jinnytest@gmail.com", "Phone": "123-456-7890",
"Position": "Engineer", "Years": "2", "Referrer": "LinkedIn",
"Degree": "BA in Computer Science",
"Resume": "https://www.linkedin.com/in/ji-eun-jinny-yang-6bb311ab",
"Source": "https://github.com/jieunjyang/test-resume/",
"Status": "Yes", "Puzzle": "puzzle"})

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    q = request.args.get('q')
    d = request.args.get('d')
    app.logger.warning(f'q is {q} and d is {d}')
    return options[q]


@app.after_request
def after_request(response):
    if response.status_code != 500:
        request_url = request.url
        app.logger.error(f'REQUEST URL: {request_url}')
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    addr = request.remote_addr
    method = request.method
    scheme = request.scheme
    full_path = request.full_path
    app.logger.error(f'{addr} {method} {scheme} {full_path} 5xx INTERNAL SERVER ERROR\n{tb}')
    return 'bad request!'

if __name__ == '__main__':
    app.run()
