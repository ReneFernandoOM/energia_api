from flask import jsonify, current_app
from app.api import bp
from app.models import Sistema
from app.schemas import SistemaSchema


@bp.route('/sistemas/', methods=['GET'])
def get_sistemas():
    sistemas = Sistema.query.all()
    sis_sch = SistemaSchema(many=True)
    return sis_sch.dumps(sistemas)