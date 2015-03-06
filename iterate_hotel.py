from get_review import get_review
from split_text import split_text
from get_hotel_info import get_hotel_info
from store_db import make_table, insert_hotel, insert_key, insert_rating, insert_review, insert_vocab, insert_weight, sqlcmd
import time
import os

def fill_database():
	f = open("short_name.txt")
	# f = open('hotel_name.txt')
	hotel_list = f.read().split()
	f.close()
	
	hotel_info = get_hotel_info()
	insert_hotel(hotel_info)

	Entry_id = 0  # id for all reviews
	for filename in hotel_list:
		os.chdir("C:\Users\Rickz\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")
		text, Hotel_id = get_review(filename)
		key, rating, review, vocab, weight, Entry_id = split_text(text, Hotel_id, Entry_id)
		# print key[:3], rating[:3], review[:3], vocab[:3], weight[:3]
		insert_key(key)
		insert_rating(rating)
		insert_review(review)
		insert_vocab(vocab)
		insert_weight(weight)

	sqlcmd()
	print "Total entries", Entry_id	

start = time.time()

# drops existing tables and creates new ones
make_table()

fill_database()

print "elapsed = ", time.time() - start
