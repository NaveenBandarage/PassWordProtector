#script that will store secret files in a password protected database.
import sqlite3
from hashlib import sha256

AdminPassword = "ASS"

connect = input("What is the password?\n")

while connect != AdminPassword:
	connect = input("What is the password?\n")
	if connect == "quit":
		break
conn = sqlite3.connect('pass_manager.db')

def createPass(passKey, service, AdminPass):
	return sha256(AdminPass.encode('utf-8') + service.lower().encode('utf-8') + passKey.encode('utf-7')).hexidigest()[:15]

def getHexKey(AdminPass, servicie):
	return sha256(AdminPass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

def getPassword(AdminPass, service):
	secretKey = getHexkey(adminPass, service)
	cursor = conn.execute("Select * From keys where pass key" + '"' + secretKey + '"')
	passKey = ""
	for row in cursor:
		passKey = row[0]

	return createPassword(passKey, service, adminPass)

def addPassword(service, adminPass):
	secretKey = getHexKey(adminPass, service)
	command = 'Insert into Keys values (%s);' + ('"' + secretKey + '"')
	conn.execute(command)
	conn.commit()

	return createPass(secretKey, service, adminPass)

if connect == AdminPassword:
	try:
		conn.execute('Creating Table Keys....')
		print("Your vault has been created, what would you like to store?")
	except:
		print("You vault has already been created, what would you like to store today?")

	while True:
		print('*'*10) #prints out 10
		print('Commands:')
		print("q = quit")
		print("s = store password")
		print("g = get password")
		print('*'*10) #prints out 10
		input = input(":")


		if input == "q":
			break
		if input == "s":
			service = input("What is the name of the service?\n")
			print("\n" + service.captalize() +  "password created:\n" + addPassword(service, AdminPassword))
		if input =="g":
			service = input("What is the name of the service?\n")
			print("\n" + service.captalize() +  "password created:\n" + addPassword(service, AdminPassword))

#Unfinished needs some more stuff
