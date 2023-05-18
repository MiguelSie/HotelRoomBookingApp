from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import dateForm, bookingForm
from app.models import Habitacion, Reserva
import pycountry

countries = [(country.name) for country in list(pycountry.countries)]
global reserva 
reserva = Reserva()

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = dateForm()
    if form.validate_on_submit():
        global reserva
        reserva.fechaInicio = form.dateStart.data
        reserva.fechaFin = form.dateFinish.data
        reserva.totPeople = form.totPeople.data
        reserva.idhabitacion = 1
        flash(f'Buscando habitaciones para {form.dateStart.data.strftime("%d/%m/%y")} hasta {form.dateFinish.data.strftime("%d/%m/%y")} para {form.totPeople.data} personas', 'success')
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
            global reserva
            reserva.name = form.name.data
            reserva.surname = form.surname.data
            reserva.email = form.email.data
            reserva.idUs = form.idUs.data
            reserva.country = form.country.data
            reserva.restaurante = form.restaurante.data
            reserva.parqueadero = form.parqueadero.data
            reserva.transporte = form.transporte.data
            reserva.lavanderia = form.lavanderia.data
            reserva.guia = form.guia.data
            db.session.add(reserva)
            db.session.commit()
            reserva = Reserva()
            flash('¡Se ha realizado su reserva exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Su reserva no se ha podido realizar.', 'danger')
    return render_template('booking.html', title='Bookings', form=form, countries = countries)
