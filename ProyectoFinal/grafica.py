import mysql.connector
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pylab as plt
import time
from time import sleep
import numpy as np


def hacer_grafica():
	miconexion = mysql.connector.connect(host="bxvwreazgf7abzi07wof-mysql.services.clever-cloud.com",user="uob136fgoyzexp57",password="gNN14QdCZ8sQhRGYno9E",database="bxvwreazgf7abzi07wof")
	micursor = miconexion.cursor()
	micursor.execute("SELECT TEMPERATURA1 FROM casa1")
	plt.figure(1)
	r1= micursor.fetchall
	temp1 = []
	n1= []
	y1=1
	for i in micursor:
		temp1.append(i)
		n1.append(y1)
		y1=y1+1
	plt.subplot2grid((3,2),(0,0))
	plt.plot(n1,temp1,"go")
	plt.title('Casa1')
	plt.ylabel('Lectura')
	
	micursor.execute("SELECT TEMPERATURA FROM casa2")
	r2=micursor.fetchall
	temp2 = []
	n2= []
	y2=1
	for i in micursor:
		temp2.append(i)
		n2.append(y2)
		y2=y2+1
	plt.subplot2grid((3,2),(0,1))
	plt.plot(n2,temp2,"bo")
	plt.title('Casa2')
	plt.ylabel('Lectura')

	micursor.execute("SELECT TEMPERATURA3 FROM casa3")
	r3=micursor.fetchall
	temp3 = []
	n3= []
	y3=1
	for i in micursor:
		temp3.append(i)
		n3.append(y3)
		y3=y3+1
	plt.subplot2grid((3,2),(1,0))
	plt.plot(n3,temp3,"ro")
	plt.title('Casa3')
	plt.ylabel('Lectura')


	micursor.execute("SELECT TEMPERATURA4 FROM casa4")
	r4=micursor.fetchall
	temp4 = []
	n4= []
	y4=1
	for i in micursor:
		temp4.append(i)
		n4.append(y4)
		y4=y4+1
	plt.subplot2grid((3,2),(1,1))
	plt.plot(n4,temp4,"yo")
	plt.title('Casa4')
	plt.xlabel('Observación cada 30 segundos')
	plt.ylabel('Lectura')


	micursor.execute("SELECT TEMPERATURA5 FROM casa5")
	r5=micursor.fetchall
	temp5 = []
	n5= []
	y5=1
	for i in micursor:
		temp5.append(i)
		n5.append(y5)
		y5=y5+1
	plt.subplot2grid((3,2),(2,0))
	plt.plot(n5,temp5,"co")
	plt.title('Casa5')
	plt.xlabel('Observación cada 30 segundos')
	plt.ylabel('Lectura')

	plt.suptitle("Temperatura")


	
	plt.figure(2)
	micursor.execute("SELECT HUMEDAD1 FROM casa1")
	r1=micursor.fetchall
	hum1 = []
	m1= []
	x1=1
	for i in micursor:
		hum1.append(i)
		m1.append(x1)
		x1=x1+1
	plt.subplot2grid((3,2),(0,0))
	plt.plot(n2,temp2,"go")
	plt.title('Casa1')
	plt.ylabel('Lectura')
	

	micursor.execute("SELECT HUMEDAD FROM casa2")
	r2=micursor.fetchall
	hum2 = []
	m2= []
	x2=1
	for i in micursor:
		hum2.append(i)
		m2.append(x2)
		x2=x2+1
	plt.subplot2grid((3,2),(0,1))
	plt.plot(n2,temp2,"bo")
	plt.title('Casa2')
	plt.ylabel('Lectura')

	micursor.execute("SELECT HUMEDAD3 FROM casa3")
	r3=micursor.fetchall
	hum3 = []
	m3= []
	x3=1
	for i in micursor:
		hum3.append(i)
		m3.append(x3)
		x3=x3+1
	plt.subplot2grid((3,2),(1,0))
	plt.plot(n2,temp2,"ro")
	plt.title('Casa3')
	plt.ylabel('Lectura')

	micursor.execute("SELECT HUMEDAD4 FROM casa4")
	r4=micursor.fetchall
	hum4 = []
	m4= []
	x4=1
	for i in micursor:
		hum4.append(i)
		m4.append(x4)
		x4=x4+1
	plt.subplot2grid((3,2),(1,1))
	plt.plot(n4,temp4,"yo")
	plt.title('Casa4')
	plt.ylabel('Lectura')
	plt.xlabel('Porcentaje de humedad')

	micursor.execute("SELECT HUMEDAD5 FROM casa5")
	r5=micursor.fetchall
	hum5 = []
	m5= []
	x5=1
	for i in micursor:
		hum5.append(i)
		m5.append(x5)
		x5=x5+1
	print(hum5)	
	plt.subplot2grid((3,2),(2,0))
	plt.plot(n5,temp5,"co")
	plt.title('Casa5')
	plt.ylabel('Lectura')	
	plt.xlabel('Porcentaje de humedad')

	plt.suptitle("Humedad")




	plt.show()

	miconexion.close()


def grafica_con(temp1,n1,temp2,n2,temp3,n3,temp4,n4,temp5,n5):
		
	fa1 = []
	f1 = []
	fa1 = temp1 
	f1 = n1
	res1 = []
	for tup in fa1:
		temp= []
		for ele in tup:
			if ele.isalpha():
				temp.append(ele)
		else:
			temp.append(float(ele))
		res1.append(temp)
	plt.figure(3)	
	plt.subplot2grid((3,2),(0,0))	
	plt.plot(f1,res1,"go")
	plt.title('Casa1')
	plt.ylabel('Lectura')

	fa2 = []
	f2 = []
	fa2 = temp2 
	f2 = n2
	res2 = []
	for tup in fa2:
		temp= []
		for ele in tup:
			if ele.isalpha():
				temp.append(ele)
		else:
			temp.append(float(ele))
		res2.append(temp)
	plt.subplot2grid((3,2),(0,1))	
	plt.plot(f2,res2,"bo")
	plt.title('Casa2')
	plt.ylabel('Lectura')

	fa3 = []
	f3 = []
	fa3 = temp3 
	f3 = n3
	res3 = []
	for tup in fa3:
		temp= []
		for ele in tup:
			if ele.isalpha():
				temp.append(ele)
		else:
			temp.append(float(ele))
		res3.append(temp)
	plt.subplot2grid((3,2),(1,0))	
	plt.plot(f3,res3,"ro")
	plt.title('Casa3')
	plt.ylabel('Lectura')
	
	fa4 = []
	f4 = []
	fa4 = temp4 
	f4 = n4
	res4 = []
	for tup in fa4:
		temp= []
		for ele in tup:
			if ele.isalpha():
				temp.append(ele)
		else:
			temp.append(float(ele))
		res4.append(temp)
	plt.subplot2grid((3,2),(1,1))	
	plt.plot(f4,res4,"yo")
	plt.title('Casa4')
	plt.xlabel('Observación')
	plt.ylabel('Lectura')

	fa5 = []
	f5 = []
	fa5 = temp5 
	f5 = n5
	res5 = []
	for tup in fa5:
		temp= []
		for ele in tup:
			if ele.isalpha():
				temp.append(ele)
		else:
			temp.append(float(ele))
		res5.append(temp)
	plt.subplot2grid((3,2),(2,0))	
	plt.plot(f5,res5,"co")
	plt.title('Casa5')
	plt.xlabel('Observación')
	plt.ylabel('Lectura')

	plt.suptitle("Conversion de temperatura °C a °F")
	plt.show()

