from numpy import divide, median, argsort, array
from math import isnan
import plotly.plotly as py
import plotly.graph_objs as objs
import pandas as pd


def plot2cluster(Hinfo, city, All=None):
    '''
    INPUT: Hinfo is a pandas dataframe and city an
           element in the 'cities' column.

    OUTPUT: Bar plot of city occurences in both clusters
    '''

    H0 = Hinfo[Hinfo['cluster'] == 0]
    H1 = Hinfo[Hinfo['cluster'] == 1]
    df0 = pd.DataFrame(H0.groupby('city').size())
    df0.columns = ['count']
    df1 = pd.DataFrame(H1.groupby('city').size())
    df1.columns = ['count']
    cities0 = df0[df0['count'] > 0]
    cities1 = df1[df1['count'] > 0]
    best_city = 'Florence_Tuscany'
    worst_city = 'Miami_Florida'
    lst = set([worst_city, city, best_city])
    cities0 = cities0.ix[lst]
    cities1 = cities1.ix[lst]
    x1med = median(H0['price'])
    x2med = median(H1['price'])
    Y0 = array([1.*y[0] for y in cities0.values])
    Y1 = array([1.*z[0] for z in cities1.values])

    for i in xrange(len(Y0)):
        if isnan(Y0[i]) or Y1[i] == 'nan':
            Y0[i] = 0.
    for j in xrange(len(Y1)):
        if isnan(Y1[j]) or Y1[j] == 'nan':
            Y1[j] = 0.
    Y_tot = Y0 + Y1
    ratio0 = divide(Y0, Y_tot)
    ratio1 = 1 - ratio0

    cluster0, cluster1 = 'High quality',  'Low quality'
    lst = [' '.join(word.split('_')) for word in lst]
    trace1 = objs.Bar(x=lst, y=ratio0, name='High ratings')
    trace2 = objs.Bar(x=lst, y=ratio1, name='Low ratings')
    data = objs.Data([trace1, trace2])
    layout = objs.Layout(
        yaxis=objs.YAxis(
            title='Proportion of counts'),
        barmode='stack')
    fig = objs.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig, filename='bar')
    return plot_url
