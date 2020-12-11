from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://readonly:ReadPass@database-bot-prueba.cinmqmovbvff.us-west-2.rds.amazonaws.com:3306/db_energia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(db.Model.metadata.tables)

# class Pm_mda(db.Model):
#     __table__ = db.Model.metadata.tables['pm_mda']

#     def __repr__(self):
#         return self.Sistema

class Sistema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    nombre = db.Column(db.String)