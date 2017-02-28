from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(Form):

    facilityTitle = "Vælg anlæg"
    #TODO Array af anlæg skal laves

    #TODO Opret alle form variabler
    roadTitle = "Vælg vejstrækning"
    roadStart = IntegerField(_name='roadStart', validators=[DataRequired()])
    roadEnd = IntegerField(_name='roadEnd', validators=[DataRequired()])

    timeTitle = "Vælg tidsvindue"
    timeStart = DateTimeField(_name='timeStart', validators=[DataRequired()])
    timeEnd = DateTimeField(_name='timeEnd', validators=[DataRequired()])
    #TODO Find ud af hvorfor submit er stylet forkert
    submit = SubmitField(_name='submit')
