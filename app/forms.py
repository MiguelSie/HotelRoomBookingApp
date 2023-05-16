from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import datetime

    
#class RoomChoiceIterable(object):
#    def __iter__(self):
#        rooms=Room.query.all()
#        yield from [(room.id,room.roomName) for room in rooms]

class dateForm(FlaskForm):
    dateStart=DateField('Fecha de inicio',validators=[DataRequired()],format='%d/%m/%Y')
    dateFinish=DateField('Fecha de fin',validators=[DataRequired()],format='%d/%m/%Y')
    totPeople=IntegerField('Cantidad de personas',validators=[DataRequired()], default=1)
    submit=SubmitField('Reservar')
    
    def validate_date(self,date):
        if self.date.data<datetime.datetime.now().date():
            raise ValidationError('You can only book for day after today.')
        
class bookingForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Nombre', validators=[DataRequired()])
    restaurante = BooleanField('Restaurante', default=True)
    parqueadero = BooleanField('Parqueadero', default=True)
    transporte = BooleanField('transporte', default=True)
    submit = SubmitField('Realizar reserva')
