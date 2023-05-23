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
        
        # Eliminar habitaciones que no cumplen con la cantidad de personas
        for habitacion in habitacionesTest:
            if habitacion in habitaciones and ((habitacion.acomodacion == "Sencilla" and form.totPeople.data > habitacion.capacidad) or (habitacion.acomodacion == "Doble" and form.totPeople.data > habitacion.capacidad)): 
                habitaciones.remove(habitacion)
        
        # Eliminar habitaciones que no están disponibles para la fecha
        acomodaciones = ["Sencilla", "Doble"]
        for acomodacion in acomodaciones:
            habitacionesAcomodacion = Habitacion.query.filter_by(acomodacion=acomodacion).all()
            for habitacion in habitacionesAcomodacion:
                if habitacion in habitaciones:
                    reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                    for reservacion in reservas:
                        if (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateFinish.data) or (reservacion.fechaInicio >= form.dateStart.data and reservacion.fechaFin <= form.dateFinish.data) or (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin > form.dateStart.data) or (reservacion.fechaInicio < form.dateFinish.data and reservacion.fechaFin >= form.dateFinish.data):
                            habitaciones.remove(habitacion)
                            break

        # Eliminar habitaciones multiples que no están disponibles para la fecha y contar la cantidad de personas que ya están reservadas
        totalMultiples = 0
        sumaReservas = 0
        for habitacion in habitacionesTest:
            if habitacion.acomodacion == "Multiple":
                reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                sumaReservas = 0
                for reservacion in reservas:
                    if (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin >= form.dateFinish.data) or (reservacion.fechaInicio >= form.dateStart.data and reservacion.fechaFin <= form.dateFinish.data) or (reservacion.fechaInicio <= form.dateStart.data and reservacion.fechaFin > form.dateStart.data) or (reservacion.fechaInicio < form.dateFinish.data and reservacion.fechaFin >= form.dateFinish.data):
                        sumaReservas += reservacion.totPeople
                if sumaReservas == habitacion.capacidad:
                    habitaciones.remove(habitacion)
                totalMultiples += sumaReservas
        totalMultiples = 50 - totalMultiples 
        
        # Avisar si no hay suficiente espacio para realizar la reserva a x personas
        if totalMultiples<form.totPeople.data and form.totPeople.data>2:
            flash(f'No hay habitaciones disponibles para {form.totPeople.data} personas en la fecha ingresada', 'danger')
            return redirect(url_for('index'))
        
        # Valida las fechas de los paros para no permitir reservar en esas fechas
        paros = Paros.query.all()
        for paro in paros:
            if (paro.fechaInicio <= form.dateStart.data and paro.fechaFin >= form.dateFinish.data) or (paro.fechaInicio >= form.dateStart.data and paro.fechaFin <= form.dateFinish.data) or (paro.fechaInicio <= form.dateStart.data and paro.fechaFin >= form.dateStart.data) or (paro.fechaInicio <= form.dateFinish.data and paro.fechaFin >= form.dateFinish.data):
                flash('No hay habitaciones disponibles para esa fecha debido al paro armado', 'danger')
                return redirect(url_for('index')) 
        
        # Si no hay habitaciones disponibles, avisa que no se puede reservar en esa fecha
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
    #Consigue los tipos de acomodaciones de las habitaciones disponibles para mostrarlas en el filtro
    for habitacion in habitaciones:
        if habitacion.acomodacion not in acomodaciones:
            acomodaciones.append(habitacion.acomodacion)
    return render_template('rooms.html', title='Rooms', habitaciones = habitaciones, acomodaciones = acomodaciones)

@app.route("/booking/Sencilla", methods = ['GET', 'POST'])
def bookSencilla():
    form = bookingForm()
    if form.validate_on_submit():
        global reserva
        fechaInicio = reserva.fechaInicio
        fechaFin = reserva.fechaFin
        totPeople = reserva.totPeople
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
        
        reservas = Reserva.query.all()
        # Valida si hay cupo en el restaurante para la fecha
        if reserva.restaurante == True:
            sumaRest = 0
            for reservacion in reservas:
                if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
                    if reservacion.restaurante == True:
                        sumaRest += reservacion.totPeople
            if sumaRest + totPeople > 40:
                flash("No hay cupo en el restaurante para esa fecha", 'danger')
                return redirect(url_for('bookSencilla'))
            cupoRestaurantes = 40 - (sumaRest + totPeople)
            print(f"cupo restaurantes ", cupoRestaurantes)
        
        #Valida si hay cupo en el parqueadero para la fecha
        if reserva.parqueadero > 0:
            sumaParqueadero = 0
            for reservacion in reservas:
                if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
                    sumaParqueadero += reservacion.parqueadero
            if sumaParqueadero + reserva.parqueadero > 25:
                flash("No hay cupo en el parqueadero para esa fecha", 'danger')
                return redirect(url_for('bookSencilla'))
            cupoParqueadero = 25 - (sumaParqueadero + reserva.parqueadero)
            print (f"cupo parqueadero ", cupoParqueadero)
            
        #Valida si hay cupo en el transporte para la fecha
        if reserva.transporte == True:
            sumaTrans = 0
            for reservacion in reservas:
                if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
                    if reservacion.transporte == True:
                        sumaTrans += reservacion.totPeople
            if sumaTrans + totPeople > 20:
                flash("No hay cupo en el transporte para esa fecha", 'danger')
                return redirect(url_for('bookSencilla'))
            cupoTransporte = 20 - (sumaTrans + totPeople)
            print(f"cupo transporte ", cupoTransporte)
        
        # Asigna a la reserva el id de la primera habitacion disponible
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
        fechaInicio = reserva.fechaInicio
        fechaFin = reserva.fechaFin
        totPeople = reserva.totPeople
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
        
        reservas = Reserva.query.all()
        # Valida si hay cupo en el restaurante para la fecha
        if reserva.restaurante == True:
            sumaRest = 0
            for reservacion in reservas:
                if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
                    if reservacion.restaurante == True:
                        sumaRest += reservacion.totPeople
            if sumaRest + totPeople > 40:
                flash("No hay cupo en el restaurante para esa fecha", 'danger')
                return redirect(url_for('bookDoble'))
            cupoRestaurantes = 40 - (sumaRest + totPeople)
            print(f"cupo restaurantes ", cupoRestaurantes)
        
        #Valida si hay cupo en el parqueadero para la fecha
        if reserva.parqueadero > 0:
            sumaParqueadero = 0
            for reservacion in reservas:
                if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
                    sumaParqueadero += reservacion.parqueadero
            if sumaParqueadero + reserva.parqueadero > 25:
                flash("No hay cupo en el parqueadero para esa fecha", 'danger')
                return redirect(url_for('bookDoble'))
            cupoParqueadero = 25 - (sumaParqueadero + reserva.parqueadero)
            print(f"cupo parqueadero ", cupoParqueadero)
            
        #Valida si hay cupo en el transporte para la fecha
        if reserva.transporte == True:
            sumaTrans = 0
            for reservacion in reservas:
                if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
                    if reservacion.transporte == True:
                        sumaTrans += reservacion.totPeople
            if sumaTrans + totPeople > 20:
                flash("No hay cupo en el transporte para esa fecha", 'danger')
                return redirect(url_for('bookDoble'))
            cupoTransporte = 20 - (sumaTrans + totPeople)
            print(f"cupo transporte ", cupoTransporte)
        
        # Asigna a la reserva el id de la primera habitacion disponible
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
        totPeopleReferencia = totPeople
        j = 0
        # Busca la cantidad de gente que tiene la habitacion multiple en esa fecha y, acorde a eso, asigna el total de gente a la habitación
        # y si todavía hay más gente por acomodar, busca la siguiente habitación multiple y así sucesivamente
        for habitacion in habitaciones:
            if habitacion.acomodacion == "Multiple" and totPeople > 0:
                j += 1
                reservas = Reserva.query.filter_by(idhabitacion=habitacion.id).all()
                sumaReservas = 0
                for reservacion in reservas:
                    if (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin >= fechaFin) or (reservacion.fechaInicio >= fechaInicio and reservacion.fechaFin <= fechaFin) or (reservacion.fechaInicio <= fechaInicio and reservacion.fechaFin > fechaInicio) or (reservacion.fechaInicio < fechaFin and reservacion.fechaFin >= fechaFin):
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
                if j == 1:
                    reservas2 = Reserva.query.all()
                    #Valida si hay cupo en el restaurante para la fecha
                    if reserva.restaurante == True:
                        sumaRest = 0
                        for reservacion2 in reservas2:
                            if (reservacion2.fechaInicio <= fechaInicio and reservacion2.fechaFin >= fechaFin) or (reservacion2.fechaInicio >= fechaInicio and reservacion2.fechaFin <= fechaFin) or (reservacion2.fechaInicio <= fechaInicio and reservacion2.fechaFin > fechaInicio) or (reservacion2.fechaInicio < fechaFin and reservacion2.fechaFin >= fechaFin):
                                if reservacion2.restaurante == True:
                                    sumaRest += reservacion2.totPeople
                        if sumaRest + totPeopleReferencia > 40:
                            flash("No hay cupo en el restaurante para esa fecha", 'danger')
                            return redirect(url_for('bookMultiple'))
                        cupoRestaurante = 40 - (sumaRest + totPeopleReferencia)
                        print(f"cupo restaurante ", cupoRestaurante)
                    
                    #Valida si hay cupo en el parqueadero para la fecha
                    if reserva.parqueadero > 0:
                        sumaParqueadero = 0
                        for reservacion2 in reservas2:
                            if (reservacion2.fechaInicio <= fechaInicio and reservacion2.fechaFin >= fechaFin) or (reservacion2.fechaInicio >= fechaInicio and reservacion2.fechaFin <= fechaFin) or (reservacion2.fechaInicio <= fechaInicio and reservacion2.fechaFin > fechaInicio) or (reservacion2.fechaInicio < fechaFin and reservacion2.fechaFin >= fechaFin):
                                sumaParqueadero += reservacion2.parqueadero
                        if sumaParqueadero + reserva.parqueadero > 25:
                            flash("No hay cupo en el parqueadero para esa fecha", 'danger')
                            return redirect(url_for('bookMultiple'))
                        cupoParqueadero = 25 - (sumaParqueadero + reserva.parqueadero)
                        print(f"cupo parqueadero ", cupoParqueadero)
                        
                    #Valida si hay cupo en el transporte para la fecha
                    if reserva.transporte == True:
                        sumaTrans = 0
                        for reservacion2 in reservas2:
                            if (reservacion2.fechaInicio <= fechaInicio and reservacion2.fechaFin >= fechaFin) or (reservacion2.fechaInicio >= fechaInicio and reservacion2.fechaFin <= fechaFin) or (reservacion2.fechaInicio <= fechaInicio and reservacion2.fechaFin > fechaInicio) or (reservacion2.fechaInicio < fechaFin and reservacion2.fechaFin >= fechaFin):
                                if reservacion2.transporte == True:
                                    sumaTrans += reservacion2.totPeople
                        if sumaTrans + totPeopleReferencia > 20:
                            flash("No hay cupo en el transporte para esa fecha", 'danger')
                            return redirect(url_for('bookMultiple'))
                        cupoTransporte = 20 - (sumaTrans + totPeopleReferencia)
                        print(f"cupo transporte ", cupoTransporte)
                        
                db.session.add(reserva)
                db.session.commit()
                reserva = Reserva()

        flash('¡Se ha realizado su reserva exitosamente!', 'success')
        return redirect(url_for('index'))
    return render_template('booking.html', title='Bookings', form=form, countries = countries)
