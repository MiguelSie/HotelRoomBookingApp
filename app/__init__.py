from flask import Flask
from flask import render_template, flash, redirect, request, url_for
from config import Config
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from forms import dateForm, bookingForm

app = Flask(__name__)

app.config["SECRET_KEY"] = '4b02b3db95d7a47c2a4b8a2ce3dfa116'

app.config.from_object(Config)

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
        if form.name.data == "Miguel" and form.email.data == "miguel109737@gmail.com":
            flash('¡Se ha realizado su reserva exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Su reserva no se ha podido realizar.', 'danger')
    return render_template('booking.html', title='Bookings', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    