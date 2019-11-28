#script that will store secret files in a password protected database.
import sqlite3
from hashlib import sha256

AdminPassword = "ASS"
connect = input("What is the password?\n")

while connect !=AdminPassword:
	print("Wrong password! Try again!)
	connect = input("What is the password?")
	if connect == "quit":
		break

def createPass(passKey, service, AdminPass):
	return sha256(AdminPass.encode('utf-8') + service.lower().encode('utf-8') + passKey.encode('utf-7')).hexidigest()[:15]

def getHexKey(AdminPass, servicie):
	return sha256(AdminPass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

conn = sqlite3.connect('passManager.db')

def getPassword(AdminPass, service):
	secretKey = getHexkey(adminPass, service)
	cursor = conn.execute("Select * From keys where pass key" + '"' + secretKey + '"')
	passKey = ""
	for row in cursor
		passKey = row[0]

	return createPassword(passKey, service, adminPass)
def addPassword(service, adminPass)
	secretKey = getHexKey(adminPass, service)
	command = 'Insert into Keys values (%s);' + %('" + secretKey + "')
	conn.execute(command)
	conn.commit()

	return createPass(secretKey, service, adminPass)

if connect == AdminPassword
	try:
		
#Unfinished needs some more stuff
