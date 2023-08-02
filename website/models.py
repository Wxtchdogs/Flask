from . import db
from flask_login import UserMixin
from sqlalchemy import func

#This script is for dealing with data shown on the site. Users make notes in a one-to-many relationship. 1 user, many notes.

#Users are stored
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    #Note id's
    notes = db.relationship('Note')

#Notes are stored
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    #Notes are assigned the user's ID
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
