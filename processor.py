import mysql.connector


mydb = mysql.connector.connect(\
	host="localhost",\
	user="root",\
	passwd="",\
	database="mysql")


mycursor = mydb.cursor()

#	noted H : HOT,  RT : ROOM-TEMPERATURE,	I : ICED,	B : BIG,	S : SMALL,	
mycursor.execute('CREATE TABLE customers (Total_Order BIGINT PRIMARY KEY, Name VARCHAR(20), Note VARCHAR(200), \
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT, \
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRoll&FriedBreadStick TINYINT, OvenRoll&Egg TINYINT, OvenRoll&FriedBreadStick&Egg TINYINT,\
	EggCake TINYINT, EggCake&FriedBreadStick TINYINT, LeekDumplings TINYINT, OvenRoll&Salad TINYINT, OvenRoll&Salad&Egg TINYINT, \
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT')


print('end')

