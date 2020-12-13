from flask import current_app

from app import db, ma


class Sistema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    nombre = db.Column(db.String)


class PmlMdaSin(db.Model):
    fecha = db.Column(db.DateTime, primary_key=True)
    pml = db.Column(db.Integer)
    id_sistema = db.Column(db.Integer, db.ForeignKey('sistema.id'), primary_key=True)
    sistema = db.relationship('Sistema', backref=db.backref('pml_mda', lazy=True))