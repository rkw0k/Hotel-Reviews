import os

hotel_list = os.listdir("C:\Users\Kwok\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")[1:-1]
# hotel_list = os.listdir("C:\Users\Rickz\Dropbox\Zipfian\winter2015\hobby\TripAdvisor\Aspects")[1:-1]
f = open('hotel_name.txt', 'w')
f.truncate()
for hotel in hotel_list:
	f.writelines(hotel)
	f.write('\n')
f.close()