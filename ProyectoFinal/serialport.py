from tkinter import *
from tkinter import messagebox
import asyncio
import threading
import time
from datetime import datetime, timedelta
import serial
import db
import grafica
import mysql.connector


varcambio = 0

def leer_datos (varcambio):
    if (varcambio==1):
        ahora = datetime.now()
        ahorastring= str(ahora).format('YYYY-MM-DD-HH-MM.SS.SSS')
        list_values = []
        list_in_floats = []
        arduino = serial.Serial('com3',9600)
        arduino_data = arduino.readline()
        decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split('x')
        for item in list_values:
            list_in_floats.append(float(item))
        Temperatura = list_in_floats[0]
        Humedad = list_in_floats[1]
        arduino_data = 0
        list_in_floats.clear()
        list_values.clear()
        arduino.close()
        hilo = threading.Thread(target=db.insert_record, args=(ahorastring,Temperatura, Humedad))
        hilo.start()

def conversion():
    miconexion = mysql.connector.connect(host="bxvwreazgf7abzi07wof-mysql.services.clever-cloud.com",user="uob136fgoyzexp57",password="gNN14QdCZ8sQhRGYno9E",database="bxvwreazgf7abzi07wof")
    micursor = miconexion.cursor()
    micursor.execute("SELECT concat(((TEMPERATURA1*Casa1)/Casa2)+Casa3)AS total1 FROM casa1,Temperatura")
    r1= micursor.fetchall
    temp1 = []
    n1= []
    y1=1
    for i in micursor:
        temp1.append(i)
        n1.append(y1)
        y1 = y1+1
    

    micursor = miconexion.cursor()
    micursor.execute("SELECT concat(((TEMPERATURA*Casa1)/Casa2)+Casa3)AS total2 FROM casa2,Temperatura")
    r2= micursor.fetchall
    temp2 = []
    n2= []
    y2=1
    for i in micursor:
        temp2.append(i)
        n2.append(y2)
        y2 = y2+1
    

    micursor = miconexion.cursor()
    micursor.execute("SELECT concat(((TEMPERATURA3*Casa1)/Casa2)+Casa3)AS total3 FROM casa3,Temperatura")
    r3= micursor.fetchall
    temp3 = []
    n3= []
    y3=1
    for i in micursor:
        temp3.append(i)
        n3.append(y3)
        y3 = y3+1
   

    micursor = miconexion.cursor()
    micursor.execute("SELECT concat(((TEMPERATURA4*Casa1)/Casa2)+Casa3)AS total4 FROM casa4,Temperatura")
    r4= micursor.fetchall
    temp4 = []
    n4= []
    y4=1
    for i in micursor:
        temp4.append(i)
        n4.append(y4)
        y4 = y4+1
   

    micursor = miconexion.cursor()
    micursor.execute("SELECT concat(((TEMPERATURA5*Casa1)/Casa2)+Casa3)AS total5 FROM casa5,Temperatura")
    r5= micursor.fetchall
    temp5 = []
    n5= []
    y5=1
    for i in micursor:
        temp5.append(i)
        n5.append(y5)
        y5 = y5+1

    grafica.grafica_con(temp1,n1,temp2,n2,temp3,n3,temp4,n4,temp5,n5)
    #messagebox.showinfo("BBDD", "Conversion realizada con éxito "+ " " + "TEMPERATURA: " + str(Temperatura) + " "+ "°C" + " "+ "TEMPERATURA: " + str(Fahrenhet)+ " " + "°F" )         