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

Vocab: (Entry_id, Aspect_id, vocab_word)

Weight: (Entry_id, Value, Room, Location, Cleanliness, FrontDesk, Service, BusinessService)

'''

# import numpy as np
# import itertools
# from get_review import get_review
# import re
# hotel_regex = re.compile(r"_[\d]+_")
# vocab_regex = re.compile(r"([\w]+)")

def split_text(text, Hotel_id, Entry_id=0):
	''' 

	INPUT: Text and hotel_id from one set of reviews from <filename>

	OUTPUT: Arrays of tuples to be inserted into tables of
	Key, Hotel_info, Rating, Review, Aspect.

	USAGE: 
	filename = r"hotel_72572_parsed_parsed.txt"
	text, Hotel_id = get_review(filename)
	key, rating, review, vocab, weight = split_text(text, Hotel_id)

	'''

	firstN = len(text) / 14 
	# firstN = 3 # first review if firstN = 1

	key_tuple = [[0, 0, '']] * firstN
	rating_tuple = [[0, 0, 0, 0, 0, 0, 0, 0, 0]] * firstN
	review_tuple = [[0, '', '']] * firstN
	vocab_tuple = []
	weight_tuple = [[0, 0, 0, 0, 0, 0, 0, 0]] * firstN

	for i in xrange(firstN):
		''' Store the first firstN ratings for into tuples to be inserted into a sql table. '''

		Entry_id += 1

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
					vocab_tuple.append(tuple([Entry_id, j + 1] + [raw_vocab[k]]))

		key_tuple[i] = (Entry_id, int(Hotel_id), Author_id)
		rating_tuple[i] = tuple(([Entry_id] + [int(Rating[0][-1])] + map(int, Rating[1:-1])))
		review_tuple[i] = tuple((Entry_id, Review_date, Content))
		weight_tuple[i] = tuple([Entry_id] + one_rating)

	return tuple(key_tuple), tuple(rating_tuple), tuple(review_tuple), tuple(vocab_tuple), tuple(weight_tuple), Entry_id



"""
debug code
# print "key:", key
# print "review:", review
# print "rating:", rating
# print "(Entry_id, Aspect_id, vocab_word):", "\n", vocab
# print "weights:", weight
"""