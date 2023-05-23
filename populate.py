from app import app,db
from datetime import datetime
from datetime import date
from app.models import *

#Creando habitaciones ordinarias y sencillas
habitacion = Habitacion(id = '1', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '2', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '3', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '4', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '5', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '6', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '7', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '8', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '9', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '10', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '11', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '12', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '13', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '14', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '15', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

habitacion = Habitacion(id = '16', tipo='Ordinaria', acomodacion='Sencilla', capacidad=1, precio=100000)
db.session.add(habitacion)

#Creando habitaciones ordinarias y dobles
habitacion = Habitacion(id = '17', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '18', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '19', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '20', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '21', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '22', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '23', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '24', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '25', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '26', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '27', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '28', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '29', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '30', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '31', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

habitacion = Habitacion(id = '32', tipo='Ordinaria', acomodacion='Doble', capacidad=2, precio=200000)
db.session.add(habitacion)

#Creando habitaciones para uso compartido
habitacion = Habitacion(id = '33', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '34', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '35', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '36', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '37', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '38', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '39', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '40', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '41', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

habitacion = Habitacion(id = '42', tipo='Compartido', acomodacion='Multiple', capacidad=5, precio=50000)
db.session.add(habitacion)

#Añadiendo un paro de prueba
paro = Paros(id = '1', fechaInicio = date(2024, 1, 3), fechaFin = date(2024, 1, 3))
db.session.add(paro)

'''
#Llenando reservas en una fecha
#Reservas sencillas
reserva = Reserva(id = '1', 
                idhabitacion = '1', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '2', 
                idhabitacion = '2', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '3', 
                idhabitacion = '3', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '4', 
                idhabitacion = '4', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '5', 
                idhabitacion = '5', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '6', 
                idhabitacion = '6', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '7', 
                idhabitacion = '7', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '8', 
                idhabitacion = '8', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '9', 
                idhabitacion = '9', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '10', 
                idhabitacion = '10', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '11', 
                idhabitacion = '11', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '12', 
                idhabitacion = '12', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '13', 
                idhabitacion = '13', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '14', 
                idhabitacion = '14', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '15', 
                idhabitacion = '15', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '16', 
                idhabitacion = '16', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

#Se llenan las dobles
reserva = Reserva(id = '17', 
                idhabitacion = '17', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '18', 
                idhabitacion = '18', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '19', 
                idhabitacion = '19', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '20', 
                idhabitacion = '20', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '21', 
                idhabitacion = '21', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '22', 
                idhabitacion = '22', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '23', 
                idhabitacion = '23', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '24', 
                idhabitacion = '24', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '25', 
                idhabitacion = '25', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '26', 
                idhabitacion = '26', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '27', 
                idhabitacion = '27', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '28', 
                idhabitacion = '28', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '29', 
                idhabitacion = '29', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '30', 
                idhabitacion = '30', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '31', 
                idhabitacion = '31', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '32', 
                idhabitacion = '32', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

#Reservas múltiples
reserva = Reserva(id = '33', 
                idhabitacion = '33', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '34', 
                idhabitacion = '34', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '35', 
                idhabitacion = '35', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '36', 
                idhabitacion = '36', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '37', 
                idhabitacion = '37', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '38', 
                idhabitacion = '38', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '39', 
                idhabitacion = '39', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '40', 
                idhabitacion = '40', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '41', 
                idhabitacion = '41', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '42', 
                idhabitacion = '42', 
                fechaInicio = date(2023, 6, 1), 
                fechaFin = date(2023, 6, 2), 
                totPeople = '5',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = False,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

#Llenando reservas en fecha distinta pero con servicios casi llenos para probar
reserva = Reserva(id = '43', 
                idhabitacion = '1', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '44', 
                idhabitacion = '2', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '45', 
                idhabitacion = '3', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '46', 
                idhabitacion = '4', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '47', 
                idhabitacion = '5', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '48', 
                idhabitacion = '6', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '49', 
                idhabitacion = '7', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '50', 
                idhabitacion = '8', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '51', 
                idhabitacion = '9', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '52', 
                idhabitacion = '10', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '53', 
                idhabitacion = '11', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '54', 
                idhabitacion = '12', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '55', 
                idhabitacion = '13', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '56', 
                idhabitacion = '14', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '57', 
                idhabitacion = '15', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '58', 
                idhabitacion = '16', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '59', 
                idhabitacion = '17', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 2,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

#Transporte tiene 19 usuarios en esta fecha, al igual que parqueadero y restaurante
reserva = Reserva(id = '60', 
                idhabitacion = '18', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = True,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '61', 
                idhabitacion = '19', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 2,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '62', 
                idhabitacion = '20', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 2,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

#Aquí parqueadero tiene 24, al igual que restaurante
reserva = Reserva(id = '63', 
                idhabitacion = '21', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 1,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '64', 
                idhabitacion = '22', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '65', 
                idhabitacion = '23', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '66', 
                idhabitacion = '24', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '67', 
                idhabitacion = '25', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '68', 
                idhabitacion = '26', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '69', 
                idhabitacion = '27', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

reserva = Reserva(id = '70', 
                idhabitacion = '28', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '2',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)

#Restaurante queda con 39
reserva = Reserva(id = '71', 
                idhabitacion = '29', 
                fechaInicio = date(2023, 6, 3), 
                fechaFin = date(2023, 6, 4), 
                totPeople = '1',
                email = 'miguel109737@gmail.com',
                name = 'Miguel',
                surname = 'Sierra',
                idUs = '100',
                country = 'Colombia',
                restaurante = True,
                transporte = False,
                parqueadero = 0,
                lavanderia = True,
                guia = True,
                pago = True)
                
db.session.add(reserva)
'''

db.session.commit()