''' 
Extract array of Overall + Aspects (7) from get_review()
Overall 0, Value 1, Room 2, Location 3, Cleanliness 4, 
Check In/Front Desk 5, Service 6, Business service 7 
overall, value, room, loc, clean, check, serv, biz = aspect
Split according to databases for insertion.

Key: (Entry_id, Hotel_id, Author_id)

Hotel_info: (Hotel_id, Price, Location)

Review: (Entry_id, Review_date, Content)

Rating: (Entry_id, Overall, Value, Room, Location, Cleanliness, FrontDesk, Service, BusinessService)

# Vocab: (Entry_id, Value_id, Room_id, Location_id, Cleanliness_id, FrontDesk_id, Service_id, BusinessService_id)

# Vocab: (Entry_id, Aspect_id)

Vocab: (Entry_id, Aspect_id, word)

Weight: (Entry_id, Value, Room, Location, Cleanliness, FrontDesk, Service, BusinessService)

'''

# import numpy as np
import itertools
import re
from get_review import get_review
# hotel_regex = re.compile(r"_[\d]+_")
vocab_regex = re.compile(r"([\w]+)")

def split_text(text, Hotel_id, Entry_id=0):
	''' 

	INPUT: Text and hotel_id from one set of reviews from <filename>

	OUTPUT: Arrays of tuples to be inserted into tables of
	Key, Hotel_info, Rating, Review, Aspect.

	USAGE: 
	filename = r"../../Aspects/hotel_72572_parsed_parsed.txt"
	text, Hotel_id = get_review(filename)
	key, review, rating, vocab, weight = split_text(text, Hotel_id)


	'''
	key_tuple = []
	review_tuple = []
	rating_tuple = []
	vocab_tuple = []
	word_tuple = []
	weight_tuple = []

	# firstN = len(text) / 14 
	firstN = 2 # first review if firstN = 1

	for i in xrange(firstN):
		''' Store the first firstN ratings for into tuples to be inserted into a sql table. '''

		Entry_id += 1

		Author_id = text[14 * i ][0][8:]
		Content = text[14 * i + 1][0][9:]
		Review_date = text[14 * i + 2][0][6:]
		Rating = text[14 * i + 3]
		Aspect_all = text[14 * i + 5 : 14 * i + 12]
		one_rating = []

		for j in xrange(7):
			raw_vocab = Aspect_all[j][1:-1]
			one_rating.append(int(Aspect_all[j][0]))
			for k in xrange(len(raw_vocab)):
				if len(raw_vocab[k]) > 0:
					word_entry = tuple([Entry_id, j + 1] + [raw_vocab[k]])
					word_tuple.append(word_entry)

		key_tuple.append((Entry_id, int(Hotel_id), Author_id))
		rating_tuple.append(tuple(([Entry_id] + [Rating[0][-1]] + Rating[1:-1])))
		review_tuple.append(tuple((Entry_id, Review_date, Content)))

		weight_tuple.append(tuple([Entry_id] + one_rating))

		# print "key_tuple", key_tuple[x]
		# print "review_tuple", review_tuple[x]
		# print "rating_tuple", rating_tuple[x]
		# print "vocab_tuple", vocab_tuple[x]
		# print "weight_tuple", weight_tuple[x]

	return tuple(key_tuple), tuple(review_tuple), tuple(rating_tuple), tuple(word_tuple), tuple(weight_tuple)

filename = r"../../Aspects/hotel_72572_parsed_parsed.txt"
text, Hotel_id = get_review(filename)
key, review, rating, vocab,  weight = split_text(text, Hotel_id)
print "key:", key
print "review:", review
print "rating:", rating
print "(Entry_id, Aspect_id, vocab_word):", "\n", vocab
print "weights:", weight