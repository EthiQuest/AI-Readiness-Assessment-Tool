from flask import Blueprint, send_from_directory
from backend import create_app

bp = Blueprint('main', __name__)
app = create_app()

@bp.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@bp.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)