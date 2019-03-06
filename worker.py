from flask import Flask, request
# from flask_debug import Debug
import mysql.connector
import json
import re



mydb = mysql.connector.connect(\
	host="localhost",\
	user="root",\
	passwd="",\
	database="mysql")


mycursor 	= 	mydb.cursor(buffered=True)

mycursor.execute('describe CookingOrder')
#	get Cooking columns
CookingCols = []
for col in mycursor:
	CookingCols.append(col)


app = Flask(__name__)
# Debug(app)

@app.route('/customer_order', methods=['POST'])
def customer_order():
	req 	= json.loads(request.data.decode('utf-8'))
	print(type(req))
	print(req)
	return ''


@app.route('/worker_finish', methods=['POST'])
def worker_finish():
	return 'Hello, World'


@app.route('/worker_update', methods=['POST'])
def worker_update():
	return 'Hello, World'


@app.route('/worker_abort', methods=['POST'])
def worker_abort():
	return 'Hello, World'


@app.route('/')
def hello_world():
	tmp=10/0;
	return 'Hello, World'


if __name__ == "__main__":
	app.run(debug=True, use_debugger=True, use_reloader=True)

print('end')

