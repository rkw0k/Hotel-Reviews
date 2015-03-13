''' 
Extract array of Overall + Aspects (7) from get_review()
Overall 0, Value 1, Room 2, Location 3, Cleanliness 4, 
Check In/Front Desk 5, Service 6, Business service 7 
overall, value, room, loc, clean, check, serv, biz = aspect
Split according to databases for insertion.

Key: (hotel_id, entry_id, author)

Hotel_info: (hotel_id, price, location)

Review: (hotel_id, entry_id, date, content)

Rating: (hotel_id, entry_id, overall, value, room, location, cleanliness, frontdesk, service, business)

Vocab: (hotel_id, entry_id, aspect_id, vocab_word)

Weight: (hotel_id, entry_id, value, room, location, cleanliness, frontdesk, service, business)

'''

# import numpy as np
# import itertools
# import re
# hotel_regex = re.compile(r"_[\d]+_")
# vocab_regex = re.compile(r"([\w]+)")

# dependency for debug
from get_review import get_review
import os

conn = 

def split_table_aspect(text, hotel_id, entry_id=0):
	''' 

	INPUT: Table Aspect_vocab from hotels.db 

	OUTPUT: A new table splitting the word column <weight(term):count> into 3 columns

	USAGE: 

	'''

	pass





"""
	firstN = len(text) / 14 
	# firstN = 3 # first review if firstN = 1

	hid = int(hotel_id)

	print '%.4f complete' % ( int(entry_id) / 200000.) 

	key_tuple = [[0, 0, '']] * firstN
	rating_tuple = [[0, 0, 0, 0, 0, 0, 0, 0, 0]] * firstN
	review_tuple = [[0, '', '']] * firstN
	vocab_tuple = []
	weight_tuple = [[0, 0, 0, 0, 0, 0, 0, 0]] * firstN

	for i in xrange(firstN):
		''' Store the first firstN ratings for into tuples to be inserted into a sql table. '''

		entry_id += 1

		# store the entire into separate temp variables
		Author_id = text[14 * i ][0][8:]
		Content = text[14 * i + 1][0][9:]
		Rating = text[14 * i + 3]
		Review_date = text[14 * i + 2][0][6:]
		Aspect = text[14 * i + 5 : 14 * i + 12]
		
		one_rating = []
		for j in xrange(7):
			''' loop through aspects: value, room, location, ... '''
			one_rating.append(int(Aspect[j][0]))
			raw_vocab = Aspect[j][1:-1]
			for k in xrange(len(raw_vocab)):
				# store all the words important to each aspect
				if len(raw_vocab[k]) > 0:
					# only store if words are found
					vocab_tuple.append(tuple([hid, entry_id, j + 1] + [raw_vocab[k]]))

		key_tuple[i] = (hid, entry_id, Author_id)
		rating_tuple[i] = tuple([hid, entry_id, int(Rating[0][-1])] + map(int, Rating[1:-1]))
		review_tuple[i] = tuple((hid, entry_id, Review_date, Content))
		weight_tuple[i] = tuple([hid, entry_id] + one_rating)

	return tuple(key_tuple), tuple(rating_tuple), tuple(review_tuple), tuple(vocab_tuple), tuple(weight_tuple), entry_id



debug code
uncomment dependencies

os.chdir("C:\Users\Rickz\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")
os.chdir("C:\Users\Kwok\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")
filename = r"hotel_72572_parsed_parsed.txt"
text, hotel_id = get_review(filename)	
key, rating, review, vocab, weight, entry_id = split_text(text, hotel_id, entry_id=0)

print "key:", key[-1]
print "review:", review[-1]
print "rating:", rating[-1]
print "vocab:", "\n", vocab[-1]
print "weight:", weight[-1]


"""