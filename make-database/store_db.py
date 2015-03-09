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

Below is a list of Table: column names

Key: (hotel_id, entry_id, author)

Hotel_info: (hotel_id, price, location)

Review: (hotel_id, entry_id, date, content)

Rating: (hotel_id, entry_id, overall, value, room, location, cleanliness, frontdesk, service, business)

Vocab: (hotel_id, entry_id, aspect_id, vocab_word)

Weight: (hotel_id, entry_id, value, room, location, cleanliness, frontdesk, service, business)


"""

def make_table(cur):

	# drop tables if exists to create new tables

	cur.execute('DROP TABLE IF EXISTS Key')
	cur.execute('DROP TABLE IF EXISTS Hotel_info;')
	cur.execute('DROP TABLE IF EXISTS Rating')
	cur.execute('DROP TABLE IF EXISTS Review')
	cur.execute('DROP TABLE IF EXISTS Aspect_vocab')
	cur.execute('DROP TABLE IF EXISTS Aspect_weight')

	# create table with the nonempty data from <filename>

	cur.execute('''CREATE TABLE Hotel_info
				   (hotel_id INT,
				    price INT,
				    location TEXT) ''')

	cur.execute('''CREATE TABLE Key
				   (hotel_id INT,
				   	entry_id INT,
				    author TEXT) ''')

	cur.execute('''CREATE TABLE Rating 
				   (hotel_id INT,
				   	entry_id INT,
					overall INT,
					value INT,
					room INT,
					location INT,
					cleanliness INT,
					frontdesk INT,
					service INT,
					business INT )''')

	cur.execute('''CREATE TABLE Review
				   (hotel_id INT,
				   	entry_id INT,
				    rdate TEXT,
				    content TEXT) ''')

	cur.execute(''' CREATE TABLE Aspect_vocab
					(hotel_id INT,
					 entry_id INT,
					 aspect_id INT,
					 word VARCHAR(255) )''')

	cur.execute('''CREATE TABLE Aspect_weight
				   (hotel_id INT,
				   	entry_id INT,
					value INT,
					room INT,
					location INT,
					cleanliness INT,
					frontdesk INT,
					service INT,
					business INT )''')


def insert_hotel(cur, hotel_info):
	qHotel_info = '''INSERT INTO Hotel_info VALUES (?,?,?) '''
	cur.executemany(qHotel_info, hotel_info)

def insert(cur, key, rating, review, vocab, weight):
	qKey = ''' INSERT INTO Key VALUES(?,?,?)'''
	qRating = ''' INSERT INTO Rating VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?) '''
	qReview = ''' INSERT INTO Review VALUES(?, ?, ?, ?) '''
	qVocab = ''' INSERT INTO Aspect_vocab VALUES(?, ?, ?, ?) '''
	qWeight = ''' INSERT INTO Aspect_weight VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) '''
	cur.executemany(qKey, key)
	cur.executemany(qRating, rating)
	cur.executemany(qReview, review)	
	cur.executemany(qVocab, vocab)
	cur.executemany(qWeight, weight)

def sqlcmd(cur):
	# cur.execute("SELECT * FROM Key;")
	# cur.execute("SELECT * FROM Rating;")
	# cur.execute("SELECT * FROM Review;")
	# cur.execute("SELECT * FROM Aspect_vocab;")
	# cur.execute("SELECT * FROM Aspect_weight LIMIT 10;")
	cur.execute("SELECT * FROM Hotel_info;")
	rows = cur.fetchall()
	print rows

