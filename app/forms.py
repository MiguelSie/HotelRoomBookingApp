from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import datetime 

class dateForm(FlaskForm):
    dateStart = DateField('Fecha de inicio',validators=[DataRequired()],format='%m/%d/%Y')
    dateFinish = DateField('Fecha de fin',validators=[DataRequired()],format='%m/%d/%Y')
    totPeople=IntegerField('Cantidad de personas',validators=[DataRequired()], default=1)
    submit=SubmitField('Reservar')
    
    def validate_dateStart(self, dateStart):
        if self.dateStart.data<datetime.datetime.now().date():
            raise ValidationError('Solo puedes reservar una fecha a partir de hoy')
        
    def validate_dateFinish(self, dateFinish):
        if self.dateStart.data>self.dateFinish.data:
            raise ValidationError('Ingrese una fecha válida')
    
        
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
