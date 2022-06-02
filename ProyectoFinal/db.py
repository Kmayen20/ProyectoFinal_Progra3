import mysql.connector
from tkinter import *
from tkinter import messagebox

def insert_record(FECHA1, TEMP, HUM):
    miconexion=mysql.connector.connect(host="bxvwreazgf7abzi07wof-mysql.services.clever-cloud.com",user="uob136fgoyzexp57",password="gNN14QdCZ8sQhRGYno9E",database="bxvwreazgf7abzi07wof")
    micursor = miconexion.cursor()
    micursor.execute ("""INSERT INTO casa1 (FECHA1, TEMPERATURA1, HUMEDAD1) VALUES (%s, %s, %s)""",(FECHA1,TEMP,HUM))
    miconexion.commit()
    w = str(FECHA1)
    h =str(w)[0:17]
    messagebox.showinfo("BBDD", "Registro agregado con éxito "+ "FECHA: " + str(h) + " " + "TEMPERATURA: " + str(TEMP) + " "+ "°C" + " "+ "HUMEDAD: " + str(HUM)+ " " + "%" )
    miconexion.close()


def crear():
    try:
     miconexion=mysql.connector.connect(host="bxvwreazgf7abzi07wof-mysql.services.clever-cloud.com",user="uob136fgoyzexp57",password="gNN14QdCZ8sQhRGYno9E",database="bxvwreazgf7abzi07wof")
     micursor = miconexion.cursor()
     sql= """ CREATE TABLE  casa1 (FECHA1 VARCHAR(50), TEMPERATURA1 DECIMAL, HUMEDAD1 DECIMAL) """
     micursor.execute (sql)
     messagebox.showinfo("BBDD", "Base de Datos creada con éxito")
     miconexion.close()
     micursor.close()
    except:
     messagebox.showwarning("¡Atención!", "La Base de Datos ya existe")