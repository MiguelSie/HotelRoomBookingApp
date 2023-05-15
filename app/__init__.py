from flask import Flask
from flask import render_template, flash, redirect, request, url_for
from config import Config
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/book')
def book():
    return render_template('booking.html', title='Bookings')

if __name__ == '__main__':
    app.run(debug=True)
    