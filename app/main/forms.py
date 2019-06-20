from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, IntegerField, SubmitField
from wtforms import validators, ValidationError

class GenerateForm(FlaskForm):
    number = IntegerField('Number of Paragraphs:', [validators.NumberRange(min=1, max=10)], default = 1)
    size = RadioField('Size of Paragraphs:', choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default = 'small')
    submit = SubmitField('Generate')