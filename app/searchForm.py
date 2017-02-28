from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(Form):

    facilityTitle = "Vælg anlæg"
    #TODO Array af anlæg skal laves

    #TODO Der skal oprettes placeholder tekst i alle input felter
    roadTitle = "Vælg start- og slutpunkt på vejstrækningen:"
    roadStart = IntegerField(_name='roadStart', validators=[DataRequired()], render_kw={"placeholder": "0000000"})
    roadEnd = IntegerField(_name='roadEnd', validators=[DataRequired()], render_kw={"placeholder": "0000000"})

    timeTitle = "Vælg start- og sluttidspunkt for tidsvinduet:"
    timeStart = DateTimeField(_name='timeStart', validators=[DataRequired()], render_kw={"placeholder": "YY-MM-DD HH:MM:SS"})
    timeEnd = DateTimeField(_name='timeEnd', validators=[DataRequired()], render_kw={"placeholder": "YY-MM-DD HH:MM:SS"})
    #TODO Find ud af hvorfor submit er stylet forkert
    submit = SubmitField(_name='submit')
