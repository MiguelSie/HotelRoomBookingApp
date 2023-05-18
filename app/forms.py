from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import datetime 

class dateForm(FlaskForm):
    dateStart = DateField('Fecha de inicio',validators=[DataRequired()],format='%m/%d/%Y')
    dateFinish = DateField('Fecha de fin',validators=[DataRequired()],format='%m/%d/%Y')
    totPeople=IntegerField('Cantidad de personas',validators=[DataRequired()], default=1)
    submit=SubmitField('Reservar')
    
    def validate_date(self,date):
        if self.dateStart.data<datetime.date.today() or self.dateFinish.data<self.dateStart.data:
            raise ValidationError('Solo puedes reservar una fecha a partir de hoy')
        
class bookingForm(FlaskForm):
    #dateStart = DateField('Fecha de inicio',validators=[DataRequired()],format='%m/%d/%Y')
    #dateFinish = DateField('Fecha de fin',validators=[DataRequired()],format='%m/%d/%Y')
    #totPeople=IntegerField('Cantidad de personas',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Nombre', validators=[DataRequired()])
    surname = StringField('Apellido', validators=[DataRequired()])
    idUs = IntegerField('Identificación', validators=[DataRequired()])
    country = StringField('País de nacimiento', validators=[DataRequired()])
    restaurante = BooleanField('Restaurante', default=True)
    parqueadero = BooleanField('Parqueadero', default=True)
    transporte = BooleanField('Transporte', default=True)
    lavanderia = BooleanField('Lavandería', default=True)
    guia = BooleanField('Guía turístico', default=True)
    submit = SubmitField('Realizar reserva')
