from DMCard.db import db

class Solicitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    income = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    credit = db.Column(db.Float, nullable=False)
    score = db.Column(db.Integer, nullable=False)
