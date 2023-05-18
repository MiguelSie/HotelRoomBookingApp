from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import dateForm, bookingForm
from app.models import Habitacion, Reserva
import pycountry

countries = [(country.name) for country in list(pycountry.countries)]

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = dateForm()
    if form.validate_on_submit():
        flash(f'Buscando vuelos para {form.dateStart.data} a {form.dateFinish.data} para {form.totPeople.data} personas', 'success')
        return redirect(url_for('book'))
    #Necesito poder pasar la información de las fechas a room para que se compare con las fechas de reserva de las habitaciones (y con las fechas de paro de las habitaciones)
    #O no sé si hacer la query de las habitaciones disponibles acá y se la paso a room para que las muestre o si hacerla allá enseguida.
    return render_template('index.html', title='Home', form=form)

@app.route('/rooms', methods = ['GET', 'POST'])
def rooms():
    #Puedo hacer que encuentre las habitaciones disponibles en las fechas que se ingresen y, que a partir de ahí
    #Escoja una de esas habitaciones y que esa sea la que se muestre en la página de habitaciones, pero sin el número,
    #De forma que se muestre la información de la habitación, pero no el número de la habitación. 
    #Esto se realiza una vez por tipo, y tener en cuenta la capacidad de la habitación. Esto también se manda a booking como parte de la info. de reserva.
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
