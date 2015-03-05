''' 
Get array of Overall + Aspects (7) from get_review()
Overall 0, Value 1, Room 2, Location 3, Cleanliness 4, 
Check In/Front Desk 5, Service 6, Business service 7 
overall, value, room, loc, clean, check, serv, biz = aspect
Split according to databases for insertion.

Key: (Entry_id, Hotel_id, Author_id)

Review: (Entry_id, Review_date, Content)
Rating: (Entry_id, Overall, Value, Room, Location, Cleanliness, \
		FrontDesk, Service, BusinessService)
Aspect: (Entry_id, Value, Room, Location, Cleanliness, FrontDesk, \
		Service, BusinessService, Weight1, Weight2, Weight3,   \
		Weight4, Weight5, Weight6, Weight7)
'''

from get_review import get_review


import numpy as np

# text, Hotel_id = get_review(filename)

def split_text(text, Hotel_id, Entry_id=0):
	''' 
	
	INPUT: Text and hotel_id from one set of reviews from <filename>

	OUTPUT: Array of tuples to be inserted into tables of
			Key, Hotel_info, Rating, Review, Aspect.
	
	'''
	key_tuple = []
	hotel_info_tuple = []
	review_tuple = []
	rating_tuple = []
	aspect_tuple = []

	# firstN = len(text) / 14 
	firstN = 1 # first review if firstN = 1
	Author_id = [0*firstN]
	Content = [0*firstN]
	Review_date = [0*firstN]
	Rating_overall = np.zeros(firstN)
	Rating = [[[], [], [], [], [], [], [], []] * firstN]
	Aspect_all = [[[], [], [], [], [], [], [], []] * firstN]

	for x in xrange(firstN):
		''' 
		Store the first firstN ratings for into arrays/tuples to be inserted into a sql table later
		'''

		Entry_id += 1
		Author_id[x] = text[14 * x ][0][8:]
		Content[x] = text[14 * x + 1][0][9:]
		Review_date[x] = text[14 * x + 2][0][6:]
		Rating[x] = text[14 * x + 3]
		Aspect_all[x] = text[14 * x + 5 : 14 * x + 12]

		one_aspect_vocab = []
		one_aspect_rating = []
		for j in xrange(7):
			one_aspect_vocab.append(Aspect_all[0][j][1:-1])
			one_aspect_rating.append(Aspect_all[0][j][0])

		aspect_tuple.append(tuple([Entry_id] + one_aspect_vocab + one_aspect_rating))

		key_tuple.append((Entry_id, Hotel_id, Author_id[x]))
		review_tuple.append((Entry_id, Review_date[x], Content[x]))
		rating_tuple.append(tuple([Entry_id] + [Rating[x][0][-1]] + Rating[x][1:-1]))


	# aspect = [[]]
	# for j in xrange(8):
	# 	# drop missing values indicated by -1 
	#     aspect.append(filter(lambda a: a != -1, variables[j]))

	# aspect.pop(0)
	# return aspect
	
	# print "Entry_id", Entry_id
	# print "Author_id", Author_id
	# print "Hotel_id", Hotel_id
	
	# print "Content", Content
	# print "Review_date", Review_date
	print "key_tuple", key_tuple
	print "review_tuple", review_tuple	
	print "rating_tuple", rating_tuple
	print "aspect_tuple", aspect_tuple

filename = r"../../Aspects/hotel_72572_parsed_parsed.txt"
text, Hotel_id = get_review(filename)
split_text(text, Hotel_id)
# x = 2
# words = text[14 * x + 5 : 14 * x + 12]
# print [words[k][0] for k in xrange(7)]





"""
	# every review consists of 14 entries 
	# overall, value, room, loc, clean, check, serv, biz
	Example of one review for one filename
	(['<Author>OGuyz'],
 ['<Content>Awsome "boutique" hotel I booked this hotel while in AZ on business. I got a GREAT price on Hotels.com (almost 1/2 price on a 24 hr sale).I have to admit that when I first pulled up outside my responce to my GPS saying you have reached your destination was...LIKE HELL I HAVE! But, then i went into the lobby and any concerns I had were washed away....It was awsome. (but get someone in to finish the marble installation on the Front Desk...It really does look unfinished)Amenities were great, Room 228 was CLEAN, mini fridge was froze over butno issue with that, Great huge flat screen TV\'s, pool beautiful staff was friendly (even the one house keeper who could only say I no speak english.  My only negative....I do not mind that you have all of your rooms nonsmoking, I even understand it. BUT, Allow people to smoke on the balcony or near the pool. It really isnt fair to make someone go down 2 flights of stairs, out the front door nd across the street to smoke.Had you description said this was a NONSMOKING PROPERTY i probably would not have choosen it. But I am glad I experienced it once.  '],
 ['<Date>May 14, 2008'],
 ['<Rating>5', '5', '5', '3', '5', '5', '3', '3', ''],
 ['<Aspects>'],
 ['0', ''],
 ['6',
  '19(price):2',
  '44(experience):1',
  '619(glad):1',
  '1464(hr):1',
  '1723(sale):1',
  '3056(hotels.com):1',
  ''],
 ['41',
  '0(staff):1',
  '3(clean):1',
  '12(friendly):1',
  '20(look):1',
  '22(pool):2',
  '26(people):1',
  '31(front):2',
  '35(street):1',
  '36(desk):1',
  '45(beautiful):1',
  '54(door):1',
  '102(near):1',
  '116(tv):1',
  '127(speak):1',
  '133(huge):1',
  '152(english):1',
  '191(balcony):1',
  '233(flight):1',
  '265(issue):1',
  '281(house):1',
  '282(negative):1',
  '291(amenity):1',
  '294(mind):1',
  '318(fridge):1',
  '359(allow):1',
  '391(understand):1',
  '448(mini):1',
  '468(smoke):2',
  '526(screen):1',
  '535(flat):1',
  '568(stair):1',
  '705(marble):1',
  '739(fair):1',
  '772(finish):1',
  '978(nonsmoking):1',
  '1321(freeze):1',
  '2377(isnt):1',
  '4147(keeper):1',
  '4628(nd):1',
  '6971(unfinished):1',
  '9102(installation):1',
  ''],
 ['12',
  '18(book):1',
  '98(outside):1',
  '147(business):1',
  '623(boutique):1',
  '851(reach):1',
  '858(pull):1',
  '1092(destination):1',
  '1282(admit):1',
  '1918(hell):1',
  '3215(awsome):1',
  '5444(gps):1',
  '7983(az):1',
  ''],
 ['5',
  '178(probably):1',
  '214(property):1',
  '978(nonsmoking):1',
  '2034(description):1',
  '12529(choosen):1',
  ''],
 ['0', ''],
 ['4', '55(lobby):1', '496(concern):1', '811(wash):1', '3215(awsome):1', ''])
"""	

# Rating1[x] = text[14 * x + 3][1]
# Rating2[x] = text[14 * x + 3][2]
# Rating3[x] = text[14 * x + 3][3]
# Rating4[x] = text[14 * x + 3][4]
# Rating5[x] = text[14 * x + 3][5]
# Rating6[x] = text[14 * x + 3][6]
# Rating7[x] = text[14 * x + 3][7]
# Aspect1[x] = text[14 * x + 5]
# Aspect2[x] = text[14 * x + 6]
# Aspect3[x] = text[14 * x + 7]
# Aspect4[x] = text[14 * x + 8]
# Aspect5[x] = text[14 * x + 9]
# Aspect6[x] = text[14 * x + 10]
# Aspect7[x] = text[14 * x + 11]
# Weight1[x] = Aspect1[x][0]
# words = text[5:12]
# print [words[k][0] for k in xrange(7)]
