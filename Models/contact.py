from Utils.database import db

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email