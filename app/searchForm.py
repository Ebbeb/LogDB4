from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(Form):
    facilityTitle = "Vælg anlæg"
    #TODO Array af anlæg skal laves

    #TODO Opret alle form variabler
    roadTitle = "Vælg vejstrækning"
    roadStart = IntegerField(_name='roadStart', validators=[DataRequired(), Length(min=7, max=7, message="Forkert input")])
    roadEnd = IntegerField(_name='roadEnd', validators=[DataRequired(), Length(min=7, max=7, message="Forkert input")])

    timeTitle = "Vælg tidsvindue"
    timeStart = DateTimeField(_name='timeStart', validators=[DataRequired()])
    timeEnd = DateTimeField(_name='timeEnd', validators=[DataRequired()])
    #TODO Find ud af hvorfor submit er forkert stylet
    submit = SubmitField(_name='submit')
