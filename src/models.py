from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from .extensions import db


# this is the model for the database

# register model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50), unique=False, nullable=False)
    lastname = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(200), primary_key=False, nullable=False)
    email = db.Column(db.String(75), nullable=False, unique=True)
    address = db.Column(db.String(75), unique=False, nullable=False)
    state = db.Column(db.String(75), unique=False, nullable=False)
    lga = db.Column(db.String(75), unique=False, nullable=False)
    phone = db.Column(db.Numeric, unique=True, nullable=True)
    bvn = db.Column(db.Numeric, nullable=True)
    usertype = db.Column(db.String, nullable=False, unique=False)
    donated_amount = db.relationship('Donated', foreign_keys='Donated.donated_by_id',
                                     backref='donator', lazy=True)

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view password')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password, method='sha256')


#donate model
class Donated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donate_amount = db.Column(db.Numeric)
    donated_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
