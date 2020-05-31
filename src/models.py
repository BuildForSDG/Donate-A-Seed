from flask_login import UserMixin
#from werkzeug.security import generate_password_hash

from .extensions import db


# this is the model for the database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(75))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    #password = db.Column(db.String(190))
    email = db.Column(db.String(75))
    address = db.Column(db.String(75))
    state = db.Column(db.String(75))
    lga = db.Column(db.String(75))
    phone = db.Column(db.Integer)
    bvn = db.Column(db.Numeric)
    farmer = db.Column(db.Boolean)
    seeder = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

    donated_amount = db.relationship('Donated', foreign_keys='Donated.donated_by_id',
                                     backref='donator', lazy=True)

   # @property
    #def unhashed_password(self):
        #raise AttributeError('Cannot view password')

    #@unhashed_password.setter
    #def unhashed_password(self, unhashed_password):
       # self.password = generate_password_hash(unhashed_password)


class Donated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donate_amount = db.Column(db.Numeric)
    donated_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
