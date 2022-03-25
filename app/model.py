from app import db

class Property(db.Model):
    property_id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(),unique = True)
    no_of_rooms = db.Column(db.String())
    no_of_bath = db.Column(db.String())
    location = db.Column(db.Text())
    price = db.Column(db.Text())
    property_type = db.Column(db.Text())
    description = db.Column(db.Text())
    photo = db.Column(db.Text())