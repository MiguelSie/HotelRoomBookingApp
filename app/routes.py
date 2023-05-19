from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import dateForm, bookingForm
from app.models import *
import pycountry

countries = [(country.name) for country in list(pycountry.countries)]
global reserva 
reserva = Reserva()

global habitaciones 
habitaciones = []

global acomodaciones
acomodaciones = []

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = dateForm()
    if form.validate_on_submit():
        global habitaciones
        habitaciones = Habitacion.query.all()

        global acomodaciones
        for habitacion in habitaciones:
            if habitacion.acomodacion not in acomodaciones:
                acomodaciones.append(habitacion.acomodacion)

        for acomodacion in acomodaciones:
            habitacionesAcomodacion = Habitacion.query.filter_by(acomodacion=acomodacion).all()
            for habitacion in habitacionesAcomodacion:
                reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                for reservacion in reservas:
                    if (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateFinish.data) or (reservacion.fechaInicio >= form.dateStart.data and reservacion.fechaFin <= form.dateFinish.data) or (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateStart.data) or (reservacion.fechaInicio <= form.dateFinish.data and reservacion.fechaFin >= form.dateFinish.data) or (habitacion.acomodacion == "Sencilla" and form.totPeople.data > habitacion.capacidad) or (habitacion.acomodacion == "Doble" and form.totPeople.data > habitacion.capacidad):
                        habitaciones.remove(habitacion)
                        break
                    
        totalMultiples = sum(
            1
            for habitacion in habitaciones
            if habitacion.acomodacion == "Multiple"
        )
        
        if totalMultiples<form.totPeople.data and form.totPeople.data>2:
            flash(f'No hay habitaciones disponibles para {form.totPeople.data} personas', 'danger')
            return redirect(url_for('index'))
        
        paros = Paros.query.all()
        for paro in paros:
            if (paro.fechaInicio <= form.dateStart.data and paro.fechaFin >= form.dateFinish.data) or (paro.fechaInicio >= form.dateStart.data and paro.fechaFin <= form.dateFinish.data) or (paro.fechaInicio <= form.dateStart.data and paro.fechaFin >= form.dateStart.data) or (paro.fechaInicio <= form.dateFinish.data and paro.fechaFin >= form.dateFinish.data):
                flash('No hay habitaciones disponibles para esa fecha debido al paro armado', 'danger')
                return redirect(url_for('index')) 
        
        if habitaciones.count == 0:
            flash('No hay habitaciones disponibles para esa fecha', 'danger')
            return redirect(url_for('index'))
        
        global reserva
        reserva.fechaInicio = form.dateStart.data
        reserva.fechaFin = form.dateFinish.data
        reserva.totPeople = form.totPeople.data
        reserva.idhabitacion = 1
        flash(f'Buscando habitaciones para {form.dateStart.data.strftime("%d/%m/%y")} hasta {form.dateFinish.data.strftime("%d/%m/%y")} para {form.totPeople.data} personas', 'success')
        return redirect(url_for('rooms'))

    return render_template('index.html', title='Home', form=form)

@app.route('/rooms', methods = ['GET', 'POST'])
def rooms():
    return render_template('rooms.html', title='Rooms', habitaciones = habitaciones, acomodaciones = acomodaciones)

@app.route("/booking/Sencilla", methods = ['GET', 'POST'])
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
            reserva.pago = True
            db.session.add(reserva)
            db.session.commit()
            reserva = Reserva()
            flash('¡Se ha realizado su reserva exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Su reserva no se ha podido realizar.', 'danger')
    return render_template('booking.html', title='Bookings', form=form, countries = countries)
