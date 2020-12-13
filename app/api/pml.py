from flask import jsonify, current_app
from app import db
from app.api import bp
from app.models import PmlMdaSin, Sistema
from app.schemas import PmlMdaSinSchema
from webargs import fields, validate
from webargs.flaskparser import use_args, parser

pml_args = {
    'id_sistema': fields.Int(required=True),
    'min_date': fields.Date(required=True),
    'max_date': fields.Date(missing='2020-12-31')
}

@bp.route('/pml/', methods=['GET'])
@use_args(pml_args, location='querystring')
def get_pml_data(args):
    print(args)
    pmlmda_schema = PmlMdaSinSchema(many=True)
    pml_data = db.session.query(PmlMdaSin).join(Sistema, PmlMdaSin.id_sistema==Sistema.id)\
        .filter(PmlMdaSin.id_sistema==args['id_sistema']).filter(PmlMdaSin.fecha>=args['min_date'])\
        .order_by(PmlMdaSin.fecha.asc()).all()
    return pmlmda_schema.dumps(pml_data)
