from app import db

class Habitacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(20), nullable=False)
    acomodacion = db.Column(db.String(20), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
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
    parqueadero = db.Column(db.Integer, nullable=False)
    lavanderia = db.Column(db.Boolean, nullable=False)
    guia = db.Column(db.Boolean, nullable=False)
    pago = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f"Reserva('{self.idhabitacion}', '{self.fechaInicio}', '{self.fechaFin}', '{self.totPeople}', '{self.email}', '{self.name}', '{self.surname}', '{self.idUs}', '{self.country}', '{self.restaurante}', '{self.transporte}', '{self.parqueadero}', '{self.lavanderia}', '{self.guia}')"


class Paros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechaInicio = db.Column(db.Date, nullable=False)
    fechaFin = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f"Paro('{self.fechaInicio}', '{self.fechaFin}')"