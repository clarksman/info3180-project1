from flask import redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField ,FileField, SubmitField
from wtforms.validators import data_required
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired


class AddPropertyForm(FlaskForm):
    property_title = StringField('Title', validators=[data_required()])
    no_of_rooms = StringField('Number Of Bedroom(s)', validators=[data_required()])
    no_of_bath = StringField('Number Of Bathroom(s)', validators=[data_required()])
    location = StringField('Location', validators=[data_required()])
    price = StringField('Price', validators=[data_required()])
    property_type = SelectField(u'Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = StringField('Description', widget=TextArea())
    photo = FileField('Property Image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Add Property')