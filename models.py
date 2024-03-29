from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_variables = {}
with open("db.env", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        db_variables[key] = value

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_variables["POSTGRES_USER"]}@contacts-db/{db_variables["POSTGRES_DB"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):


    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    def __repr__(self):
        return '<Contacts %r>' % self.name
