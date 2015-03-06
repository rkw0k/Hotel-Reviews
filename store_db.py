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

Key: Entry_id, Hotel_id, Author_id

Hotel_info: Hotel_id, Price, Location

Review: Entry_id, Review_date, Content

Rating: Entry_id, Overall, Value, Room, Location, Cleanliness, 
		Front_desk, Service, BusinessService

Vocab: (Entry_id, Value_id, Room_id, Location_id, Cleanliness_id, FrontDesk_id, Service_id, BusinessService_id)

Weight: (Entry_id, Value, Room, Location, Cleanliness, FrontDesk, Service, BusinessService)
"""
from get_review import get_review
from split_text import split_text
from get_hotel_info import get_hotel_info
import sqlite3 as lite

conn = lite.connect('hotels.db')
conn.text_factory = str
cur = conn.cursor()

def make_table():

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

	cur.execute('''CREATE TABLE Aspect_vocab
				   (Entry_id INT,
					Value_id INT,
					Room_id INT,
					Location_id INT,
					Cleanliness_id INT,
					FrontDesk_id INT,
					Service_id INT,
					BusinessService_id INT )''')

	cur.execute(''' CREATE TABLE Vocab_words
					(Entry_id INT,
					 Aspect_id INT,
					 Word TEXT )''')

	cur.execute('''CREATE TABLE Aspect_weight
					(Entry_id INT,
					Value INT,
					Room INT,
					Location INT,
					Cleanliness INT,
					FrontDesk INT,
					Service INT,
					BusinessService INT )''')

def insert_hotel_table(hotel_info):
	query = '''INSERT INTO Hotel_info VALUES (?,?,?) 
			'''
	cur.executemany(query, hotel_info)
	# cur.execute("SELECT * FROM Hotel_info;")
	rows = cur.fetchall()
	print rows

def insert_key_table(key):
	query = ''' INSERT INTO Key VALUES(?,?,?)'''
	cur.executemany(query, key)
	# cur.execute("SELECT * FROM Key;")
	rows = cur.fetchall()
	print rows

def insert_review_table(review):
	query = ''' INSERT INTO Review VALUES(?, ?, ?) '''
	cur.executemany(query, review)
	cur.execute("SELECT * FROM Review;")
	rows = cur.fetchall()
	print rows

def insert_rating_table(rating):
	query = ''' INSERT INTO Rating VALUES(?, ?, ?, ?, ?, ?, ?, ?,?) '''
	cur.executemany(query, rating)
	cur.execute("SELECT * FROM Rating;")
	rows = cur.fetchall()
	print rows

def insert_vocab_table(vocab):
	query = ''' INSERT INTO Aspect_vocab VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
	cur.executemany(query, vocab)
	cur.execute("SELECT * FROM Aspect_vocab;")
	rows = cur.fetchall()
	print rows

make_table()
# hotel_info = get_hotel_info()
# insert_hotel_table(hotel_info)


filename = r"../../Aspects/hotel_72572_parsed_parsed.txt"
text, Hotel_id = get_review(filename)
key, review, rating, vocab, weight = split_text(text, Hotel_id)
print vocab[:3]
# insert_key_table(key)
# insert_review_table(review)
# insert_rating_table(rating)
# insert_vocab_table(vocab)
# insert_weight_table(weight)
