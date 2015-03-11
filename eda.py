import pandas as pd
import sqlite3 as lite
import numpy as np
from scipy.spatial.distance import cdist, cosine
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
# % matplotlib inline
# connect to database and load all the tables into separate dataframes
conn = lite.connect("../hotels.db")
weight = pd.read_sql("SELECT * FROM Aspect_weight;", conn)
key = pd.read_sql("SELECT * FROM Key;", conn)
rating = pd.read_sql("SELECT * FROM Rating;", conn)
hinfo = pd.read_sql("SELECT * FROM H_info;", conn) # contains averages for ratings
cities = pd.read_sql("select distinct(location) from H_info;", conn).values

# Warning, vocab and review are heavy on memory
# vocab = pd.read_sql("SELECT * FROM Aspect_vocab;", conn)
# review = pd.read_sql("SELECT * FROM Review;", conn)
# conn.close()

# connect to database and load all the tables into separate dataframes
aspects = ['value', 'room', 'location', 'cleanliness']

def avg_rating(hid, aspects):
    overall, value, room, location, cleanliness = aspects
    avgRating_q = """select %s, %s, %s, %s, %s from H_info 
            where hotel_id = %d; """ % (overall, value, room, location, cleanliness, hid)
    vec = pd.read_sql(avgRating_q, conn).values[0][0]
    if vec:
        return vec
    return

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

def plot_two_hotel(Hinfo1, Hinfo2):
    len1 = len(Hinfo1)
    len2 = len(Hinfo2)
    x1, O1, V1, R1, L1, C1 = np.zeros(len1), np.zeros(len1), np.zeros(len1), np.zeros(len1), np.zeros(len1), np.zeros(len1)
    x2, O2, V2, R2, L2, C2 = np.zeros(len2), np.zeros(len2), np.zeros(len2), np.zeros(len2), np.zeros(len2), np.zeros(len2)
    for i in xrange(len1):
        hid, x1[i], loc, O1[i], V1[i], R1[i], L1[i], C1[i] = Hinfo1[i]
        
    for j in xrange(len2):
        hid, x2[j], loc, O2[j], V2[j], R2[j], L2[j], C2[j] = Hinfo2[j]
        
    x1mean, O1mean, V1mean, R1mean, L1mean, C1mean = np.mean(x1), np.mean(O1), np.mean(V1), np.mean(R1), np.mean(L1), np.mean(C1)
    x2mean, O2mean, V2mean, R2mean, L2mean, C2mean = np.mean(x2), np.mean(O2), np.mean(V2), np.mean(R2), np.mean(L2), np.mean(C2)
    
    label1 = "%s, hotel_count=%d" % (loc1, len1)
    label2 = "%s, hotel_count=%d" % (loc2, len2)
    
    # big overall plot
    fig = plt.figure(figsize=(20,4))
    # scatterplot of the ratings against price
    plt.scatter(x1, O1, color='red', alpha=0.2, label=label1) 
    # marker
    plt.scatter(x1mean, O1mean, color='red', marker='x', s=150, linewidths=5)  
    plt.scatter(x2, O2, color='blue', alpha=0.2, label=label2) 
    plt.scatter(x2mean, O2mean, color='blue', marker='x', s=150, linewidths=5)
    plt.xlabel('Price')
    plt.ylabel('average Aspect:Overall')
    maxO1, maxO2 = np.max(O1), np.max(O2)
    plt.ylim([np.min(O1), max(maxO1, maxO2) + 1])
    fig.tight_layout()
    plt.legend()
    
    # Four subplots for Value, Room, Location, Cleanliness ratings for each location
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 7))
    ax1.scatter(x1, V1, color='red', alpha=0.2)
    ax1.scatter(x1mean, V1mean, color='red', marker='x', s=150, linewidths=5)
    ax1.scatter(x2, V2, color='blue', alpha=0.2)
    ax1.scatter(x2mean, V2mean, color='blue', marker='x', s=150, linewidths=5)
    ax1.set_xlabel('price')
    ax1.set_ylabel('average Aspect:Value')
    maxV1, maxV2 = np.max(V1), np.max(V2)
    ax1.set_ylim([1., 5.5])
#     ax1.set_ylim([np.min(V1), max(maxV1, maxV2) + 0.5])
    
    ax2.scatter(x1, R1, color='red', alpha=0.2)
    ax2.scatter(x1mean, R1mean, color='red', marker='x', s=150, linewidths=5)
    ax2.scatter(x2, R2, color='blue', alpha=0.2)
    ax2.scatter(x2mean, R2mean, color='blue', marker='x', s=150, linewidths=5)
    ax2.set_xlabel('price')
    ax2.set_ylabel('average Aspect:Room')
    maxR1, maxR2 = np.max(R1), np.max(R2)
    ax2.set_ylim([1., 5.5])
#     ax2.set_ylim([np.min(R1), max(maxR1, maxR2) + 0.5])
    
    ax3.scatter(x1, L1, color='red', alpha=0.2)
    ax3.scatter(x1mean, L1mean, color='red', marker='x', s=150, linewidths=5)
    ax3.scatter(x2, L2, color='blue', alpha=0.2)
    ax3.scatter(x2mean, L2mean, color='blue', marker='x', s=150, linewidths=5)
    ax3.set_xlabel('price')
    ax3.set_ylabel('average Aspect:Location')
    maxL1, maxL2 = np.max(L1), np.max(L2)
    ax3.set_ylim([1., 5.5])
#     ax3.set_ylim([np.min(L1), max(maxL1, maxL2) + 0.5])
    
    ax4.scatter(x1, C1, color='red', alpha=0.2)
    ax4.scatter(x1mean, C1mean, color='red', marker='x', s=150, linewidths=5)
    ax4.scatter(x2, C2, color='blue', alpha=0.2)
    ax4.scatter(x2mean, C2mean, color='blue', marker='x', s=150, linewidths=5)
    ax4.set_xlabel('price')
    ax4.set_ylabel('average Aspect:Cleanliness')
    maxC1, maxC2 = np.max(C1), np.max(C2)
    ax4.set_ylim([1., 5.5])
#     ax4.set_ylim([np.min(C1), max(maxC1, maxC2) + 0.5])
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    fig.tight_layout()

plot_two_hotel(Hinfo1, Hinfo2)    
    
# aspect = 'location'
Hinfo_NOLA = get_hotel_info('New_Orleans_Louisiana')
Hinfo_SF = get_hotel_info('San_Francisco_California')
plot_two_aspect('value', Hinfo_SF, Hinfo_NOLA)


similarities = squareform(pdist(X, metric='cosine'))
print similarities[:5, :5]
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