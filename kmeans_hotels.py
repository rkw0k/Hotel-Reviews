'''
Usage: Hinfo = kmeans_hotels.get_clusters()
'''
import pandas as pd
import sqlite3 as lite
import numpy as np
from sklearn.cluster import KMeans

# connect to database
conn = lite.connect("../hotels.db")

def get_hotel_info(city=None):
    """
    INPUT: A city from H_info.city or None

    OUTPUT: The rows of H_info with hotel_id in both
            Key and itself or all of H_info.
    """
    if city:
        end = "WHERE h.city = '%s';" % city
    else:
        end = ";"
    select = '''
    SELECT h.hotel_id hotel_id, h.price price, h.city city,
    h.avgO, h.avgV, h.avgR, avgL, avgC
    FROM H_info h
    JOIN
    (SELECT DISTINCT(hotel_id)
    FROM Key) as dKey
    ON dKey.hotel_id = h.hotel_id
    '''

    return pd.read_sql(select + end, conn)


def get_avgdf():
    # normalize features of dataframe hinfo to be mean zero variance one
    Hinfo = get_hotel_info()
    column = ['price', 'avgO', 'avgV', 'avgR', 'avgL', 'avgC']
    new_column = ['p_norm', 'o_norm', 'v_norm', 'r_norm',
                  'l_norm', 'c_norm']
    for i in xrange(6):
        mean = Hinfo[column[i]].mean()
        std = Hinfo[column[i]].std()
        Hinfo[new_column[i]] = (Hinfo[column[i]] - mean) / std

    return Hinfo


def get_clusters():
    '''
    INPUT: Feature matrix consisting of hotel

    OUTPUT: Dataframe and numpy array consisting of
            clusters of hotels info trained on average
            value, rating, location, cleanliness ratings.

    NOTE: Used gap statistic and silhouette score to
          determine K=2 was the best choice for number
          of clusters in K-means
    '''
    Hinfo = get_avgdf()
    ''' Train on normalized Value, Room, Location,
        Cleanliness aspects'''
    X = Hinfo[['v_norm', 'r_norm', 'l_norm', 'c_norm']].values
    K = 2
    kmeans_model = KMeans(K, init='random', n_init=20,
                          precompute_distances=False, random_state=1)
    kmeans_model.fit(X)
    Y = kmeans_model.labels_
    Hinfo['cluster'] = np.zeros(Hinfo.shape[0])
    for k in xrange(1, K):
        Hinfo['cluster'][Y == k] = k
    return Hinfo