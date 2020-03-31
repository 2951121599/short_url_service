import sys
import importlib

importlib.reload(sys)
from apps.controler.urls_handler import is_exist_url
from flask import render_template, redirect, make_response, jsonify
from flask import Flask
from url_route import init_url_route

app = Flask(__name__)

init_url_route(app)


@app.route('/api/v1/index', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/api/v1/short/<short_url>', methods=['GET'])
def redirect_short_url(short_url):
    print('short_url:', short_url)
    long_url = is_exist_url(short_url)
    print('long_url:', long_url)
    if long_url:
        return redirect(long_url)
    return make_response(jsonify({'error': 'not find'}), 401)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10011
    app.run(host=host, port=int(port), debug=True)
