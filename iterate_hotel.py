from get_review import get_review
from split_text import split_text
from get_hotel_info import get_hotel_info
from store_db import make_table, insert_hotel, insert, sqlcmd
import time
import os
import sqlite3 as lite

def fill_database(cur):
	# f = open('hotel_name.txt')
	f = open('short_name.txt')
	hotel_list = f.read().split()
	f.close()

	hotel_info = get_hotel_info()
	insert_hotel(cur, hotel_info)

	# id for reviews
	entry_id = 0  
	for filename in hotel_list:
		os.chdir("C:\Users\Rickz\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")
		text, hotel_id = get_review(filename)
		key, rating, review, vocab, weight, entry_id = split_text(text, hotel_id, entry_id)
		insert(cur, key, rating, review, vocab, weight)

	# command to run test queries
	# sqlcmd(cur)
	print "Total entries", entry_id	

start = time.time()

# connect to sqlite database 
print "connecting to database ..."
conn = lite.connect('hotels.db')
conn.text_factory = str
cur = conn.cursor()

# drops existing tables and creates new ones then commits
print "making tables ..."
make_table(cur)

print "filling database ..."
fill_database(cur)

print "committing ..."
conn.commit()

print "elapsed = ", time.time() - start
# run time on laptop about 5 minutes for about 200,000 rows.

