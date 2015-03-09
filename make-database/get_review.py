'''
Extract text from <filename>
'''
import re

def get_review(filename):
	''' 
	
	INPUT: <filename> or path to <filename> from a 
			hotel .txt file.

	OUTPUT: Text containing all the content of filename and hotel_id
	
	'''
	f = open(filename)
	text = f.read()
	f.close()
	
	text = [word.split('\t') for word in text.splitlines()]
	str_file = str(filename)
	hotel_regex = re.compile(r"_[\d]+_")
	hotel_id = re.findall(hotel_regex, str_file)[0]

	return text, hotel_id[1:-1] 
