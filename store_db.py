""" 
This file inserts the contents of the ratings 
from <filename> into a sql database hotels.db. 
Aspect0 = Overall
Aspect1 = Value
Aspect2 = Room
Aspect3 = Location
Aspect4 = Cleanliness
Aspect5 = Checkin
Aspect6 = Service
Aspect7 = BusinessService
"""

import read_one_aspect
import sqlite3 as lite

def make_table(reviews):
	conn = lite.connect('hotels.db')
	cur = conn.cursor()

	# drop tables if exists for re-inserting
	cur.execute('DROP TABLE IF EXISTS Hotel_info')
	cur.execute('DROP TABLE IF EXISTS Review')
	cur.execute('DROP TABLE IF EXISTS Rating')
	cur.execute('DROP TABLE IF EXISTS Aspect')

	# create table with the nonempty data in <filename>
	cur.execute('''CREATE TABLE Key
				   (Entry_id INT,
				    Hotel_id INT,
				    Author_id TEXT,
				    ) ''')

	cur.execute('''CREATE TABLE Hotel_info
				   (Hotel_id INT,
				    Price INT,
				    Location TEXT,
				    ) ''')

	cur.execute('''CREATE TABLE Review
				   (Entry_id INT,
				    Review_date TEXT,
				    Content VARCHAR(MAX)
				    ) ''')


	cur.execute('''CREATE TABLE Rating 
				   (Entry_id TEXT,
					Overall INT,
					Value INT,
					Room INT,
					Location INT,
					Cleanliness INT,
					Checkin INT,
					Service INT,
					BusinessService INT
					)''')

	cur.execute('''CREATE TABLE Aspect
				   (Entry_id TEXT,
					Aspect1 TEXT,
					Aspect2 TEXT,
					Aspect3 TEXT,
					Aspect4 TEXT,
					Aspect5 TEXT,
					Aspect6 TEXT,
					Aspect7 TEXT,
					Weight1 INT,
					Weight2 INT,
					Weight3 INT,
					Weight4 INT,
					Weight5 INT,
					Weight6 INT,
					Weight7 INT
					)''')

	cur.execute(''' INSERT INTO Review VALUES 

						) ''')

def get_review(filename):
	text = read_one_aspect(filename)
	return text 
