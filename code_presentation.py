import pandas as pd
import sqlite3 as lite
import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
% matplotlib inline
# connect to database and load all the tables into separate dataframes
conn = lite.connect("../hotels.db")
rating = pd.read_sql("SELECT * FROM Rating;", conn)
hinfo = pd.read_sql("SELECT * FROM H_info;", conn) # contains averages for ratings
cities = pd.read_sql("select distinct(location) from H_info;", conn).values

cluster0, cluster1 = 'High aspect ratings',  'Low aspect ratings'

city = 'San_Francisco_California'

h0_SF = hcluster[0][hcluster[0][:, 2] == city]
h1_SF = hcluster[1][hcluster[1][:, 2] == city]
# print h0_SF, h1_SF
c0meds, c1meds = plot_two_hotel(h0_SF, h1_SF)

df0 = pd.DataFrame(h0_SF)
df0.columns = ['hotel_id', 'price', 'city', 'overall', 'value', 'room', 'location', 'cleanliness']
df0_price = df0[df0['price'] < 200]
df0_price.sort('price', ascending=True)[:20]

df1 = pd.DataFrame(h1_SF)
df1.columns = ['hotel_id', 'price', 'city', 'overall', 'value', 'room', 'location', 'cleanliness']
df1_price = df1[df1['price'] < 200]
df1_price.sort('price', ascending=True)[:20]