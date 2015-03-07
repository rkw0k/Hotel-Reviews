from get_review import get_review
from split_text import split_text
from get_hotel_info import get_hotel_info
from store_db import make_table, insert_hotel, insert_key, insert_rating, insert_review, insert_vocab, insert_weight, sqlcmd
import time
import os
import sqlite3 as lite

def fill_database(cur):
	# f = open("short_name.txt") # test on 10
	f = open('hotel_name.txt')
	hotel_list = f.read().split()
	f.close()

	hotel_info = get_hotel_info()
	insert_hotel(cur, hotel_info)

	Entry_id = 0  # id for all reviews
	for filename in hotel_list:
		os.chdir("C:\Users\Rickz\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")
		text, Hotel_id = get_review(filename)
		key, rating, review, vocab, weight, Entry_id = split_text(text, Hotel_id, Entry_id)

		insert_key(cur, key)
		insert_rating(cur, rating)
		insert_review(cur, review)
		insert_vocab(cur, vocab)
		insert_weight(cur, weight)

	# sqlcmd()
	print "Total entries", Entry_id	

start = time.time()

# connect to sqlite database 
conn = lite.connect('hotels.db')
conn.text_factory = str
cur = conn.cursor()

# drops existing tables and creates new ones
make_table(cur)

fill_database(cur)
conn.commit()
print "elapsed = ", time.time() - start
