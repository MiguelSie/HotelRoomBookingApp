from re import T
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

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():  # sourcery skip: low-code-quality, sum-comprehension
    form = dateForm()
    if form.validate_on_submit():
        global habitaciones
        habitaciones = Habitacion.query.all()
        habitacionesTest = Habitacion.query.all()
        
        for habitacion in habitacionesTest:
            if habitacion in habitaciones and ((habitacion.acomodacion == "Sencilla" and form.totPeople.data > habitacion.capacidad) or (habitacion.acomodacion == "Doble" and form.totPeople.data > habitacion.capacidad)): 
                habitaciones.remove(habitacion)
        
        acomodaciones = ["Sencilla", "Doble"]
        for acomodacion in acomodaciones:
            habitacionesAcomodacion = Habitacion.query.filter_by(acomodacion=acomodacion).all()
            for habitacion in habitacionesAcomodacion:
                if habitacion in habitaciones:
                    reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                    for reservacion in reservas:
                        if (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateFinish.data) or (reservacion.fechaInicio >= form.dateStart.data and reservacion.fechaFin <= form.dateFinish.data) or (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateStart.data) or (reservacion.fechaInicio <= form.dateFinish.data and reservacion.fechaFin >= form.dateFinish.data):
                            habitaciones.remove(habitacion)
                            break

        totalMultiples = 0
        sumaReservas = 0
        for habitacion in habitacionesTest:
            if habitacion.acomodacion == "Multiple":
                reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                sumaReservas = 0
                for reservacion in reservas:
                    if (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateFinish.data) or (reservacion.fechaInicio >= form.dateStart.data and reservacion.fechaFin <= form.dateFinish.data) or (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateStart.data) or (reservacion.fechaInicio <= form.dateFinish.data and reservacion.fechaFin >= form.dateFinish.data):
                        sumaReservas += reservacion.totPeople
                if sumaReservas == habitacion.capacidad:
                    habitaciones.remove(habitacion)
                totalMultiples += sumaReservas
        totalMultiples = 50 - totalMultiples 
        
        if totalMultiples<form.totPeople.data and form.totPeople.data>2:
            flash(f'No hay habitaciones disponibles para {form.totPeople.data} personas en la fecha ingresada', 'danger')
            return redirect(url_for('index'))
        
        paros = Paros.query.all()
        for paro in paros:
            if (paro.fechaInicio <= form.dateStart.data and paro.fechaFin >= form.dateFinish.data) or (paro.fechaInicio >= form.dateStart.data and paro.fechaFin <= form.dateFinish.data) or (paro.fechaInicio <= form.dateStart.data and paro.fechaFin >= form.dateStart.data) or (paro.fechaInicio <= form.dateFinish.data and paro.fechaFin >= form.dateFinish.data):
                flash('No hay habitaciones disponibles para esa fecha debido al paro armado', 'danger')
                return redirect(url_for('index')) 
        
        if len(habitaciones) == 0:
            flash('No hay habitaciones disponibles para esa fecha', 'danger')
            return redirect(url_for('index'))
        
        global reserva
        reserva.fechaInicio = form.dateStart.data
        reserva.fechaFin = form.dateFinish.data
        reserva.totPeople = form.totPeople.data
        
        flash(f'Buscando habitaciones para {form.dateStart.data.strftime("%d/%m/%y")} hasta {form.dateFinish.data.strftime("%d/%m/%y")} para {form.totPeople.data} personas', 'success')
        return redirect(url_for('rooms'))

    return render_template('index.html', title='Home', form=form)

@app.route('/rooms', methods = ['GET', 'POST'])
def rooms():
    global habitaciones
    acomodaciones = []
    for habitacion in habitaciones:
        if habitacion.acomodacion not in acomodaciones:
            acomodaciones.append(habitacion.acomodacion)
    return render_template('rooms.html', title='Rooms', habitaciones = habitaciones, acomodaciones = acomodaciones)

@app.route("/booking/Sencilla", methods = ['GET', 'POST'])
def bookSencilla():
    form = bookingForm()
    if form.validate_on_submit():
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
        
        for habitacion in habitaciones:
            if habitacion.acomodacion == "Sencilla":
                reserva.idhabitacion = habitacion.id
                break
        
        db.session.add(reserva)
        db.session.commit()
        reserva = Reserva()
        flash('¡Se ha realizado su reserva exitosamente!', 'success')
        return redirect(url_for('index'))
    return render_template('booking.html', title='Bookings', form=form, countries = countries)

@app.route("/booking/Doble", methods = ['GET', 'POST'])
def bookDoble():
    form = bookingForm()
    if form.validate_on_submit():
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
        
        for habitacion in habitaciones:
            if habitacion.acomodacion == "Doble":
                reserva.idhabitacion = habitacion.id
                break
        
        db.session.add(reserva)
        db.session.commit()
        reserva = Reserva()
        flash('¡Se ha realizado su reserva exitosamente!', 'success')
        return redirect(url_for('index'))
    return render_template('booking.html', title='Bookings', form=form, countries = countries)

@app.route("/booking/Multiple", methods = ['GET', 'POST'])
def bookMultiple():  # sourcery skip: low-code-quality, sum-comprehension
    form = bookingForm()
    if form.validate_on_submit():
        global reserva
        global habitaciones

        fechaInicio = reserva.fechaInicio
        fechaFin = reserva.fechaFin
        totPeople = reserva.totPeople
        print(habitaciones)
        for habitacion in habitaciones:
            if habitacion.acomodacion == "Multiple" and totPeople > 0:
                reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                sumaReservas = 0
                for reservacion in reservas:
                    if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaInicio) or (reservacion.fechaInicio <= fechaFin and reservacion.fechaFin >= fechaFin):
                        sumaReservas += reservacion.totPeople
                reserva.fechaInicio = fechaInicio
                reserva.fechaFin = fechaFin
                camasLibres = 5 - sumaReservas
                if totPeople > 5 or totPeople >= camasLibres:
                    reserva.totPeople = camasLibres
                    totPeople = totPeople - camasLibres
                else:
                    reserva.totPeople = totPeople
                    totPeople = 0
                reserva.idhabitacion = habitacion.id
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
    return render_template('booking.html', title='Bookings', form=form, countries = countries)
