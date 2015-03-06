''' 
Extract an array of Overall + Seven Aspects from filename: 
Overall 0, Value 1, Room 2, Location 3, Cleanliness 4, 
Check In/Front Desk 5, Service 6, Business service 7 
'''

def open_parsed(filename):
	'''

	INPUT: filename of one hotel file with aspects.
	
	OUTPUT: array of user's aspect reviews from filename

	example usage:
	filename = hotel_269171_parsed_parsed.txt
	aspects = open_parsed(filename)
	overall, value, room, loc, clean, check, serv, biz = aspect
	''' 
	f = open(filename)
	text = f.read()
	f.close()
	text = [word.split('\t') for word in text.splitlines()]
	return text

"""
	aspect = [[]]
	for j in xrange(8):
		# drop missing values indicated by -1 from values
	    aspect.append(filter(lambda a: a != -1, variables[j]))

	aspect.pop(0);
	return aspect
"""	
