""" 
This file inserts the contents of the ratings 
from <filename> into a sql database hotels.db. 
Aspect0 = Overall (O)
Aspect1 = Value (V)
Aspect2 = Room (R) 
Aspect3 = Location (L)
Aspect4 = Cleanliness (C)
Aspect5 = FrontDesk (F) 
Aspect6 = Service (S)
Aspect7 = BusinessService (B)
and similarly for Weight1 = Value, etc. 

Below is a list of Table: column names

Key: Entry_id, Hotel_id, Author_id

Hotel_info: Hotel_id, Price, Location

Review: Entry_id, Review_date, Content

Rating: Entry_id, Overall, Value, Room, Location, Cleanliness, \
		FrontDesk, Service, BusinessService

Aspect: Entry_id, Value, Room, Location, Cleanliness, FrontDesk, \
		Service, BusinessService, Weight1, Weight2, Weight3,   \
		Weight4, Weight5, Weight6, Weight7
"""
from get_hotel_info import get_hotel_info

import sqlite3 as lite
conn = lite.connect('hotels.db')
cur = conn.cursor()


def make_table():

	# drop tables if exists for re-inserting
	cur.execute('DROP TABLE IF EXISTS Key')
	cur.execute('DROP TABLE IF EXISTS Hotel_info')
	cur.execute('DROP TABLE IF EXISTS Review')
	cur.execute('DROP TABLE IF EXISTS Rating')
	cur.execute('DROP TABLE IF EXISTS Aspect')

	# create table with the nonempty data from <filename>
	cur.execute('''CREATE TABLE Key
				   (Entry_id INT,
				    Hotel_id INT,
				    Author_id TEXT
				    ) ''')

	cur.execute('''CREATE TABLE Hotel_info
				   (Hotel_id INT,
				    Price INT,
				    Location TEXT
				    ) ''')

	cur.execute('''CREATE TABLE Review
				   (Entry_id INT,
				    Review_date TEXT,
				    Content BLOB
				    ) ''')

	cur.execute('''CREATE TABLE Rating 
				   (Entry_id TEXT,
					Overall INT,
					Value INT,
					Room INT,
					Location INT,
					Cleanliness INT,
					FrontDesk INT,
					Service INT,
					BusinessService INT
					)''')

	cur.execute('''CREATE TABLE Aspect
				   (Entry_id TEXT,
					Value TEXT,
					Room TEXT,
					Location TEXT,
					Cleanliness TEXT,
					Front_Desk TEXT,
					Service TEXT,
					BusinessService TEXT,
					Weight1 INT,
					Weight2 INT,
					Weight3 INT,
					Weight4 INT,
					Weight5 INT,
					Weight6 INT,
					Weight7 INT
					)''')

def insert_hotel_table(hotel_info):
	for h_info in hotel_info:
		h_info = tuple(h_info)
		cur.executemany("INSERT INTO Hotel_info VALUES(?,?,?)", h_info)
	rows = cur.fetchall()
	print rows

make_table()
hotel_info = get_hotel_info()
print hotel_info[0], hotel_info[1], hotel_info[2]
# insert_hotel_table(hotel_info)
