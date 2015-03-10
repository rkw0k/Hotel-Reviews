'''
Hotel_info: 
(hotel_id, price, location, avgO, avgV, avgR, avgL, avgC)

Rating: 
(hotel_id, entry_id, overall, value, room, location, cleanliness, frontdesk, service, business)

'''

import sqlite3 as lite
conn = lite.connect('../../hotels.db')
conn.text_factory = str
cur = conn.cursor()

def replace_neg_ratings(cur):
	'''
	Create temporary table to compute averages with missing
	values replaced by the overall rating.
	'''
	drop = ''' DROP TABLE IF EXISTS Rating_filled;'''

	copy = '''CREATE TABLE Rating_filled AS
	SELECT hotel_id, overall, value, room, location, cleanliness FROM Rating;'''

	cur.execute(drop)
	cur.execute(copy)

	for rating in ['value', 'room', 'location', 'cleanliness']:
		q = ''' UPDATE Rating_filled
		SET %s = overall
		WHERE %s = -1;''' % (rating, rating)
		cur.execute(q)

def make_hotel_rating(cur):
	'''
	INPUT: Hotel_id, aspect

	OUTPUT: None. Makes table of Hotel_id with their average aspect ratings

	'''
	Rating_q = '''CREATE TABLE H_info AS
		SELECT h.hotel_id hotel_id, h.price price, h.location location, AVG(r.overall) avgO, AVG(r.value) avgV, AVG(r.room) avgR, AVG(r.location) avgL, AVG(r.cleanliness) avgC 
		FROM Rating_filled r
		JOIN Hotel_info h
		ON h.hotel_id = r.hotel_id
		GROUP BY h.hotel_id;'''

    cur.execute(Rating_q)

make_hotel_rating(cur)
# replace_neg_ratings(cur)
conn.commit()
# conn.close()

"""

"""