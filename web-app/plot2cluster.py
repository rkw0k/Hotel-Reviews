from numpy import divide, median, argsort, array
import plotly.plotly as py
from plotly.graph_objs import *

def plot2cluster(Hinfo, city, All=None):
	''' 
	INPUT: cities and hotel information

	OUTPUT: histogram of city occurences in both clusters

	For cities in each cluster, plot the distribution of locations.
	idx -> cities
	0. Sort counts in cities0 dataframe
	1. Get indices of cities0 dataframe in that order
	2. Order cities1 dataframe in that order
	'''

	H0 = Hinfo[Hinfo['cluster'] == 0]
	H1 = Hinfo[Hinfo['cluster'] == 1]
	cities0 = H0.groupby('city').size()
	cities1 = H1.groupby('city').size()
	df0 = cities0.to_frame(name='count')
	df1 = cities1.to_frame(name='count')
	cities0 = df0[df0['count'] > 10]
	cities1 = df1[df1['count'] > 10]
	best_city = 'Florence_Tuscany'
	worst_city = 'Miami_Florida'
	lst = [worst_city, city, best_city]
	cities0 = cities0.ix[lst]
	cities1 = cities1.ix[lst]
	x1med = median(H0['price'])
	x2med = median(H1['price'])
	Y0 = array([1.*y[0] for y in cities0.values])
	Y1 = array([1.*z[0] for z in cities1.values])
	ratio0 = divide(Y0, Y0 + Y1)
	ratio1 = 1 - ratio0
	idx = argsort(ratio0)
	ratio0 = ratio0[idx]
	ratio1 = ratio1[idx]

	cluster0, cluster1 = 'High quality',  'Low quality'
	lst = [' '.join(word.split('_')) for word in lst]

	trace1 = Bar(x=lst, y=ratio0, name='High ratings')
	trace2 = Bar(x=lst, y=ratio1, name='Low ratings')
	data = Data([trace1, trace2])
	layout = Layout(barmode='stack')
	fig = Figure(data=data, layout=layout)
	plot_url = py.iplot(fig, filename='bar')

   	return plot_url
