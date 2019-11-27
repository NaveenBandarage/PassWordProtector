#script that will store secret files in a password protected database.
import sqlite3
from hashlib import sha256

AdminPass = "ASS"
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
	cursor = conn.execute("Select * From keys whre pass key" + '"' + secretKey + '"'
#Unfinished needs some more stuff 
