from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.urls import url_parse
from forms import dateForm, bookingForm
import pycountry
app = Flask(__name__)

app.config["SECRET_KEY"] = '4b02b3db95d7a47c2a4b8a2ce3dfa116'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Habitacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(20), nullable=False)
    acomodacion = db.Column(db.String(20), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    fechaParo = db.Column(db.Date, nullable=False)
    reserva = db.relationship('Reserva', backref='habitacion', lazy=True)
    
    def __repr__(self):
        return f"Habitacion('{self.tipo}', '{self.acomodacion}', '{self.capacidad}', '{self.precio}')"

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idhabitacion = db.Column(db.Integer, db.ForeignKey('habitacion.id'), nullable=False)
    fechaInicio = db.Column(db.Date, nullable=False)
    fechaFin = db.Column(db.Date, nullable=False)
    totPeople = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    idUs = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(40), nullable=False)
    restaurante = db.Column(db.Boolean, nullable=False)
    transporte = db.Column(db.Boolean, nullable=False)
    parqueadero = db.Column(db.Boolean, nullable=False)
    lavanderia = db.Column(db.Boolean, nullable=False)
    guia = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f"Reserva('{self.idHabitacion}', '{self.fechaInicio}', '{self.fechaFin}', '{self.totPeople}', '{self.email}', '{self.name}', '{self.surname}', '{self.idUs}', '{self.country}', '{self.restaurante}', '{self.transporte}', '{self.parqueadero}', '{self.lavanderia}', '{self.guia}')"

countries = [(country.name) for country in list(pycountry.countries)]

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = dateForm()
    if form.validate_on_submit():
        flash(f'Buscando vuelos para {form.dateStart.data} a {form.dateFinish.data} para {form.totPeople.data} personas', 'success')
        return redirect(url_for('book'))
    return render_template('index.html', title='Home', form=form)

@app.route('/rooms', methods = ['GET', 'POST'])
def rooms():
    return render_template('rooms.html', title='Rooms')

@app.route("/booking", methods = ['GET', 'POST'])
def book():
    form = bookingForm()
    if form.validate_on_submit():
        if form.name.data == "Miguel" and form.email.data == "miguel109737@gmail.com" and form.surname.data == "Sierra":
            flash('¡Se ha realizado su reserva exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Su reserva no se ha podido realizar.', 'danger')
    return render_template('booking.html', title='Bookings', form=form, countries = countries)

if __name__ == '__main__':
    app.run(debug=True)
    