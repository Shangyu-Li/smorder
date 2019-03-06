import mysql.connector


mydb = mysql.connector.connect(\
	host="localhost",\
	user="root",\
	passwd="",\
	database="mysql")


mycursor = mydb.cursor()


#	DoneOrder table for done orders
mycursor.execute('DROP TABLE IF EXISTS DoneOrder')

#	noted H : HOT,  RT : ROOM-TEMPERATURE,	I : ICED,	B : BIG,	S : SMALL,	A : AND
mycursor.execute('CREATE TABLE DoneOrder (Total_Order BIGINT PRIMARY KEY, Datte DATE, Timme TIME, Name VARCHAR(20), Note VARCHAR(200), Period_min INT,\
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT,\
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRollFriedBreadStick TINYINT, OvenRollEgg TINYINT, OvenRollFriedBreadStickEgg TINYINT,\
	EggCake TINYINT, EggCakeFriedBreadStick TINYINT, LeekDumpling TINYINT, OvenRollSalad TINYINT, OvenRollSaladEgg TINYINT,\
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT)')


#	AbortedOrder table for abandon orders
mycursor.execute('DROP TABLE IF EXISTS AbortedOrder')

#	noted H : HOT,  RT : ROOM-TEMPERATURE,	I : ICED,	B : BIG,	S : SMALL,	A : AND
mycursor.execute('CREATE TABLE AbortedOrder (Total_Order BIGINT PRIMARY KEY, Datte DATE, Timme TIME, Name VARCHAR(20), Note VARCHAR(200), Period_min INT,\
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT,\
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRollFriedBreadStick TINYINT, OvenRollEgg TINYINT, OvenRollFriedBreadStickEgg TINYINT,\
	EggCake TINYINT, EggCakeFriedBreadStick TINYINT, LeekDumpling TINYINT, OvenRollSalad TINYINT, OvenRollSaladEgg TINYINT,\
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT)')


#	CookingOrder table for unready orders
mycursor.execute('DROP TABLE IF EXISTS CookingOrder')

#	noted H : HOT,  RT : ROOM-TEMPERATURE,	I : ICED,	B : BIG,	S : SMALL,	A : AND
mycursor.execute('CREATE TABLE CookingOrder (Total_Order BIGINT PRIMARY KEY, Datte DATE, Timme TIME, Name VARCHAR(20), Note VARCHAR(200), Period_min INT,\
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT,\
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRollFriedBreadStick TINYINT, OvenRollEgg TINYINT, OvenRollFriedBreadStickEgg TINYINT,\
	EggCake TINYINT, EggCakeFriedBreadStick TINYINT, LeekDumpling TINYINT, OvenRollSalad TINYINT, OvenRollSaladEgg TINYINT,\
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT)')