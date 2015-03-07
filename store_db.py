""" 
This file inserts the contents of the ratings 
from <filename> into a sql database hotels.db. 
Aspect0 = Overall (O)
Aspect1 = Value (V)
Aspect2 = Room (R) 
Aspect3 = Location (L)
Aspect4 = Cleanliness (C)
Aspect5 = Front_desk (F) 
Aspect6 = Service (S)
Aspect7 = BusinessService (B)
and similarly for Weight1 = Value, etc. 

Below is a list of Table: column names

Key: (Entry_id, Hotel_id, Author_id)

Hotel_info: (Hotel_id, Price, Location)

Review: (Entry_id, Review_date, Content)

Rating: (Entry_id, Overall, Value, Room, Location, Cleanliness, 
		Front_desk, Service, BusinessService)

Vocab: (Entry_id, Aspect_id, vocab_word)

Weight: (Entry_id, Value, Room, Location, Cleanliness, FrontDesk, Service, BusinessService)

"""

def make_table(cur):

	# drop tables if exists for re-inserting
	cur.execute('DROP TABLE IF EXISTS Key')
	cur.execute('DROP TABLE IF EXISTS Hotel_info;')
	cur.execute('DROP TABLE IF EXISTS Review')
	cur.execute('DROP TABLE IF EXISTS Rating')
	cur.execute('DROP TABLE IF EXISTS Aspect_vocab')
	cur.execute('DROP TABLE IF EXISTS Aspect_weight')

	# create table with the nonempty data from <filename>
	cur.execute('''CREATE TABLE Hotel_info
				   (Hotel_id INT,
				    Price INT,
				    Location TEXT) ''')

	cur.execute('''CREATE TABLE Key
				   (Entry_id INT,
				    Hotel_id INT,
				    Author_id TEXT) ''')

	cur.execute('''CREATE TABLE Rating 
				   (Entry_id INT,
					Overall INT,
					Value INT,
					Room INT,
					Location INT,
					Cleanliness INT,
					FrontDesk INT,
					Service INT,
					BusinessService INT )''')

	cur.execute('''CREATE TABLE Review
				   (Entry_id INT,
				    Review_date TEXT,
				    Content TEXT) ''')

	# cur.execute('''CREATE TABLE Aspect_vocab
	# 			   (Entry_id INT,
	# 				Value_id INT,
	# 				Room_id INT,
	# 				Location_id INT,
	# 				Cleanliness_id INT,
	# 				FrontDesk_id INT,
	# 				Service_id INT,
	# 				BusinessService_id INT )''')

	cur.execute(''' CREATE TABLE Aspect_vocab
					(Entry_id INT,
					 Aspect_id INT,
					 Word VARCHAR(255) )''')

	cur.execute('''CREATE TABLE Aspect_weight
					(Entry_id INT,
					Value INT,
					Room INT,
					Location INT,
					Cleanliness INT,
					FrontDesk INT,
					Service INT,
					BusinessService INT )''')

def insert_hotel(cur, hotel_info):
	query = '''INSERT INTO Hotel_info VALUES (?,?,?) 
			'''
	cur.executemany(query, hotel_info)
	
	# rows = cur.fetchall()
	# print rows

def insert_key(cur, key):
	query = ''' INSERT INTO Key VALUES(?,?,?)'''
	cur.executemany(query, key)
	
	# rows = cur.fetchall()
	# print rows

def insert_rating(cur, rating):
	query = ''' INSERT INTO Rating VALUES(?, ?, ?, ?, ?, ?, ?, ?,?) '''
	cur.executemany(query, rating)
	
	# rows = cur.fetchall()
	# print rows

def insert_review(cur, review):
	query = ''' INSERT INTO Review VALUES(?, ?, ?) '''
	cur.executemany(query, review)
	
	# rows = cur.fetchall()
	# print rows

def insert_vocab(cur, vocab):
	query = ''' INSERT INTO Aspect_vocab VALUES(?, ?, ?) '''
	cur.executemany(query, vocab)
	
	# rows = cur.fetchall()
	# print rows

def insert_weight(cur, weight):
	query = ''' INSERT INTO Aspect_weight VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
	cur.executemany(query, weight)

def sqlcmd(cur):
	# cur.execute("SELECT * FROM Key;")
	# cur.execute("SELECT * FROM Rating;")
	# cur.execute("SELECT * FROM Review;")
	# cur.execute("SELECT * FROM Aspect_vocab;")
	# cur.execute("SELECT * FROM Aspect_weight LIMIT 10;")
	cur.execute("SELECT * FROM Hotel_info;")
	rows = cur.fetchall()
	print rows



