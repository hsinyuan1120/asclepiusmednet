from flask import Flask, request, send_file
from app.route import index


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.add_url_rule('/', '/', index)
    
    return app

