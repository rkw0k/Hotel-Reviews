import pandas as pd
import sqlite3 as lite
import numpy as np
from scipy.spatial.distance import cdist, cosine
import matplotlib.pyplot as plt
# % matplotlib inline
# connect to database and load all the tables into separate dataframes
conn = lite.connect("../hotels.db")
aspects = ['value', 'room', 'location', 'cleanliness', 'frontdesk', 'service', 'business']

def connect():
	key = pd.read_sql("SELECT * FROM Key;", conn)
	hinfo = pd.read_sql("SELECT * FROM Hotel_info;", conn)
	rating = pd.read_sql("SELECT * FROM Rating;", conn)
	weight = pd.read_sql("SELECT * FROM Aspect_weight;", conn)
	return key, hinfo, rating, weight

def get_hotel_info(city=None):
    if city:
        end = "WHERE Hotel_info.location = '%s';" % city
    else:
        end = ";"
    select = '''
    SELECT Hotel_info.hotel_id, Hotel_info.price, Hotel_info.location
    FROM Hotel_info 
    JOIN 
    (SELECT DISTINCT(hotel_id)
    FROM Key) as dKey
    ON dKey.hotel_id = Hotel_info.hotel_id
    '''
    hotelids = pd.read_sql(select + end, conn).values
    return hotelids

def avg_aspect(hid, aspect):
    Weight_q = """select avg(%s) from Aspect_weight 
            where hotel_id = %d; """ % (aspect, hid)
    vec = pd.read_sql(Weight_q, conn).values[0][0]
    if vec:
        return vec
    else:
        return -1

def plot_two_aspect(aspect, Hinfo1, Hinfo2):
    x1, y1 = np.zeros(len(Hinfo1)), np.zeros(len(Hinfo1))
    x2, y2 = np.zeros(len(Hinfo2)), np.zeros(len(Hinfo2))
    for i in xrange(len(Hinfo1)):
        hid, price, loc = Hinfo1[i]
        x1[i] = price
        y1[i] = avg_aspect(hid, aspect)
        
    for j in xrange(len(Hinfo2)):
        hid, price, loc = Hinfo2[j]
        x2[j] = price
        y2[j] = avg_aspect(hid, aspect)
        
    fig = plt.figure(figsize=(5,10))
    plt.scatter(x1, y1, color='red', alpha=0.5)
    plt.scatter(x2, y2, color='blue', alpha=0.5)
    plt.xlabel('price')
    plt.ylabel('average Aspect:%s' % aspect)
    
# aspect = 'location'
Hinfo_NOLA = get_hotel_info('New_Orleans_Louisiana')
Hinfo_SF = get_hotel_info('San_Francisco_California')
plot_two_aspect('value', Hinfo_SF, Hinfo_NOLA)

# cities = pd.read_sql("select distinct(location) from Hotel_info;", conn).values
# aspect = 'location'
# city1 = 'New_Orleans_Louisiana'
# city2 = 'San_Francisco_California'
# Hinfo1 = get_hotel_info(city1)
# Hinfo2 = get_hotel_info(city2)
# plot_aspect(aspect, Hinfo1)
# plot_aspect(aspect, Hinfo2)

# hotelids = get_hotel_info(city=None)

# key, hinfo, rating, weight = connect()