from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import datetime

    
class RoomChoiceIterable(object):
    def __iter__(self):
        rooms=Room.query.all()
        yield from [(room.id,room.roomName) for room in rooms]
        
class BookmeetingForm(FlaskForm):
    title=StringField('Meeting title',validators=[DataRequired()])
    rooms=SelectField('Choose room',coerce=int,choices=RoomChoiceIterable())
    date=DateField('Choose date', format="%m/%d/%Y",validators=[DataRequired()])
    startTime=SelectField('Choose starting time(in 24hr expression)',coerce=int,choices=[(i,i) for i in range(9,19)])
    duration=SelectField('Choose duration of the meeting(in hours)',coerce=int,choices=[(i,i) for i in range(1,6)])
    submit=SubmitField('Book')