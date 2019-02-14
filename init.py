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
mycursor.execute('CREATE TABLE DoneOrder (Total_Order BIGINT PRIMARY KEY, Datte DATE, Timme TIME, Name VARCHAR(20), Note VARCHAR(200),\
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT,\
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRollAFriedBreadStick TINYINT, OvenRollAEgg TINYINT, OvenRollAFriedBreadStickAEgg TINYINT,\
	EggCake TINYINT, EggCakeAFriedBreadStick TINYINT, LeekDumplings TINYINT, OvenRollASalad TINYINT, OvenRollASaladAEgg TINYINT,\
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT)')


#	AbortedDish table for abandon orders
mycursor.execute('DROP TABLE IF EXISTS AbortedDish')

#	noted H : HOT,  RT : ROOM-TEMPERATURE,	I : ICED,	B : BIG,	S : SMALL,	A : AND
mycursor.execute('CREATE TABLE AbortedDish (Total_Order BIGINT PRIMARY KEY, Datte DATE, Timme TIME, Name VARCHAR(20), Note VARCHAR(200),\
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT,\
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRollAFriedBreadStick TINYINT, OvenRollAEgg TINYINT, OvenRollAFriedBreadStickAEgg TINYINT,\
	EggCake TINYINT, EggCakeAFriedBreadStick TINYINT, LeekDumplings TINYINT, OvenRollASalad TINYINT, OvenRollASaladAEgg TINYINT,\
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT)')


#	CookingDish table for unready orders
mycursor.execute('DROP TABLE IF EXISTS CookingDish')

#	noted H : HOT,  RT : ROOM-TEMPERATURE,	I : ICED,	B : BIG,	S : SMALL,	A : AND
mycursor.execute('CREATE TABLE CookingDish (Total_Order BIGINT PRIMARY KEY, Datte DATE, Timme TIME, Name VARCHAR(20), Note VARCHAR(200),\
	HB_SoyJuice TINYINT, HS_SoyJuice TINYINT, RTB_SoyJuice TINYINT, RTS_SoyJuice TINYINT, IB_SoyJuice TINYINT, IS_SoyJuice TINYINT,\
	HB_RiceJuice TINYINT, HS_RiceJuice TINYINT, RTB_RiceJuice TINYINT, RTS_RiceJuice TINYINT, IB_RiceJuice TINYINT, IS_RiceJuice TINYINT,\
	B_SavorySoyJuice TINYINT, S_SavorySoyJuice TINYINT, B_BlackTea TINYINT, S_BlackTea TINYINT,\
	OvenRoll TINYINT, FriedBreadStick TINYINT, OvenRollAFriedBreadStick TINYINT, OvenRollAEgg TINYINT, OvenRollAFriedBreadStickAEgg TINYINT,\
	EggCake TINYINT, EggCakeAFriedBreadStick TINYINT, LeekDumplings TINYINT, OvenRollASalad TINYINT, OvenRollASaladAEgg TINYINT,\
	SteamedBun TINYINT, FriedEgg TINYINT, GreenOnionEgg TINYINT)')