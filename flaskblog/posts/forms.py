from flask_wtf import FlaskForm
from mongoengine.fields import IntField
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    price = StringField('Costs')
    opening_hours = StringField('Opening hours')
    toilet_paper = BooleanField('Toilet paper available?')
    sink = BooleanField('Sink available?')
    soap = BooleanField('Soap available?')
    wheelchair_acc = BooleanField('Accessible with wheelchair?')
    toilet = BooleanField('Water closet available?')
    urinal = BooleanField('Urinal available?')
    submit = SubmitField('Post')

class RatingForm(FlaskForm):
    rating = IntegerField('Give some stars', validators=[DataRequired()])
    comment = StringField('Comment')
    submit = SubmitField('Submit your Rate')