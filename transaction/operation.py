#! /usr/bin/python3
# -*-coding : utf-8 -*-
import mysql.connector



def database():
	global conn, cursor
	conn = mysql.connector.connect(host='localhost',
									user='python', 
									password='passer', 
									database='banque', 
									auth_plugin='mysql_native_password')
	cursor = conn.cursor()
	
def create(prenom, nom, code,numcompte, solde ):
	database()
	sql = "insert into client(prenom, nom, code,numcompte, solde) values(%s, %s, %s,%s,%s)"
	val = (prenom, nom, code,numcompte, solde )
	cursor.execute(sql, val)
	conn.commit()

def readAll():
	sql = "select * from client"
	database()
	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		yield i
		
def consultation(numcompte, code):
	database()
	sql = "select * from client where numcompte=%s and code=%s"
	val = (numcompte, code)
	cursor.execute(sql, val)
	result = cursor.fetchall()
	if len(result) == 0:
		message = "donnees incorrectes"
	else:
		message = "le solde de votre compte est de " + result[0][5]
		
	return message
	
def versement(numcompte, montant):
	database()
	sql1 = "select * from client where numcompte=%s"
	cursor.execute(sql1, (numcompte, ))
	result = cursor.fetchall()
	if len(result) == 0:
		message = "ce compte n'existe pas"
	else:
		solde = result[0][5]
		solde = float(solde) + float(montant)
		solde = str(solde)
		sql = "update client set solde=%s where numcompte=%s"
		val = (solde, numcompte)
		cursor.execute(sql, val)
		#conn.commit()
		message = "Votre nouveau solde est de " + solde
	
	return message

def retrait(numcompte, montant, code):
	database()
	sql1 = "select * from client where numcompte=%s and code=%s"
	cursor.execute(sql1, (numcompte, code))
	result = cursor.fetchall()
	if len(result) == 0:
		message = "Informations erronées"
	else:
		solde = result[0][5]
		if float(montant) > float(solde):
			message= "disponibilite insuffisante"
		else:
			solde = float(solde) - float(montant)
			solde = str(solde)
			sql = "update client set solde=%s where numcompte=%s"
			val = (solde, numcompte)
			cursor.execute(sql, val)
			conn.commit()
			message = "Votre nouveau solde est de " + solde
		
	return message

def suppression(id):
	database()
	sql = "delete from client where id=%s"
	cursor.execute(sql, (id,))
	conn.commit()
	return "Compte supprimé avec succes"
	

