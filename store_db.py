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

	# drop table if it exists
	cur.execute('DROP TABLE IF EXISTS Aspect')

	# create table with the nonempty data in <filename>
	cur.execute('''CREATE TABLE Review 
				   (Author TEXT,
				    Content VARCHAR(MAX),
				    Occurrence TEXT,
				    Rating  TEXT
				    Aspect0 VARCHAR(MAX),
				    Aspect1 VARCHAR(MAX),
				    Aspect2 VARCHAR(MAX),
				    Aspect3 VARCHAR(MAX),
				    Aspect4 VARCHAR(MAX),
				    Aspect5 VARCHAR(MAX),
				    Aspect6 VARCHAR(MAX),
				    Aspect7 VARCHAR(MAX),
				    ) ''')
	cur.execute(''' INSERT INTO Review VALUES 

		''')

def get_review(filename):
	text = read_one_aspect(filename)
	return text 


"""
cur.execute('''CREATE TABLE Aspect 
			   ('Author' TEXT,
				'Content' TEXT,
				'Date' TEXT
				'OverallRating' INT,
				'Value' INT,
				'Room' INT,
				'Location' INT,
				'Cleanliness' INT,
				'Checkin' INT,
				'Service' INT,
				'BusinessService' INT,
				'Aspect'	)''')
"""