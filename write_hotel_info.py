# Hotel_info: (Hotel_id, Price, Location)

from get_hotel_info import get_hotel_info
text = get_hotel_info()

def write_hotel_info(text):
	''' 
	INPUT: text from hotel_price_location.txt
	OUTPUT: tuples consisting of (hotel_id, price, location) rows
	'''
	
	for row in text[:5]:
		print row
		
write_hotel_info(text)
