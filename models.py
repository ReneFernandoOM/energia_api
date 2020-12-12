from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from webargs import fields, validate
from webargs.flaskparser import use_args, parser
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://readonly:ReadPass@database-bot-prueba.cinmqmovbvff.us-west-2.rds.amazonaws.com:3306/db_energia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

user_args = {
    'id': fields.Int(),
    'short_name': fields.Str(),
    'name': fields.Str(),
    'date': fields.Date()
}

pml_args = {
    'id_sistema': fields.Int(required=True),
    'min_date': fields.Date(required=True),
    'max_date': fields.Date(missing='2020-12-31')
}

# class Pm_mda(db.Model):
#     __table__ = db.Model.metadata.tables['pm_mda']

#     def __repr__(self):
#         return self.Sistema

class Sistema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    nombre = db.Column(db.String)

class SistemaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sistema
    id = ma.auto_field()
    short_name = ma.auto_field()
    nombre = ma.auto_field()


class PmlMdaSin(db.Model):
    fecha = db.Column(db.DateTime, primary_key=True)
    pml = db.Column(db.Integer)
    id_sistema = db.Column(db.Integer, db.ForeignKey('sistema.id'), primary_key=True)
    sistema = db.relationship('Sistema', backref=db.backref('pml_mda', lazy=True))

class PmlMdaSinSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PmlMdaSin
    fecha = ma.auto_field()
    pml = ma.auto_field()
    id_sistema = ma.auto_field()

@app.route('/sistemas/')
def get_sistemas():
    sis_schema = SistemaSchema(many=True)
    sistemas = Sistema.query.all()
    print(sistemas)
    return sis_schema.dumps(sistemas)

@app.route('/sis/', methods=['GET'])
@use_args(user_args, location='querystring')
def get_sistema(args):
    print(args)
    sis_schema = SistemaSchema()
    # argumentos = sis_schema.load(args)
    # print(argumentos)
    sistema = Sistema.query.get(args['id'])
    print(sistema)
    return sis_schema.dumps(sistema)

@app.route('/pml/', methods=['GET'])
@use_args(pml_args, location='querystring')
def get_pml_data(args):
    print(args)
    pmlmda_schema = PmlMdaSinSchema(many=True)
    id_sis = args['id_sistema']
    pml_data = PmlMdaSin.query.filter(PmlMdaSin.id_sistema == id_sis).filter(PmlMdaSin.fecha>=args['min_date']).all()
    print(pml_data)
    return pmlmda_schema.dumps(pml_data)

if __name__ == '__main__':
    app.run(debug=True)

