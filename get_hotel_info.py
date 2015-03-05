# Hotel_info: (Hotel_id, Price, Location)

import re
hotel_regex = re.compile(r"_[\d]+_")

def get_hotel_info():
	''' 
	
	INPUT: hotel_price_location.txt 

	OUTPUT: list consisting of [hotel_id, price, location] entries
	
	'''

	f = open('../hotel_price_location.txt')
	text = f.read()
	f.close()
	text = [word.split('\t') for word in text.splitlines()]
	for i in xrange(1, len(text)):
		number = re.findall(hotel_regex, text[i][0])
		text[i][0] = number[0][1:-1]
	return text

text = get_hotel_info()
print text[5:10]