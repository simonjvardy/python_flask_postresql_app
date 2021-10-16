from app import db


class Data(db.Model):
    __tablename__="data"

    id = db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

    def __repr__(self):
        return '<id {}>'.format(self.id)
