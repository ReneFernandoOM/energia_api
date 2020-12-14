from flask import jsonify, current_app
from app.base import bp

@bp.route('/')
def index():

    return jsonify({'hello': 'world'})
