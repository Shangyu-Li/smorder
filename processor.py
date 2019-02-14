import mysql.connector


mydb = mysql.connector.connect(\
	host="localhost",\
	user="root",\
	passwd="",\
	database="mysql")


mycursor = mydb.cursor()


mycursor.execute('SELECT * FROM customers')
for x in mycursor:
	print(x)


print('end')

