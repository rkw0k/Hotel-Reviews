from flask import Flask
from flask import request
import sqlite3 as lite
from pandas import read_sql
import numpy as np
from flask import render_template
from get_table import get_table
from plot2cluster import plot2cluster


app = Flask(__name__)
@app.route('/')
def submission_page():
  ''' Homepage for app.'''
  conn = lite.connect('app.db')
  Hinfo = read_sql('select * from H_normed', conn)
  Hinfo = Hinfo.drop('index', 1)
  cities = read_sql('select * from cities', conn)
  cvalues = cities.values[:,0]
  conn.close()
  return render_template('index.html', htmltable1=cvalues)


@app.route('/plot_function', methods=['POST'])
def plot_function():
  ''' Plots plotly and table with best hotels. '''
  conn = lite.connect('app.db')
  Hinfo = read_sql('select * from H_normed', conn)
  Hinfo = Hinfo.drop('index', 1)
  submit = request.form['user_input']
  city = "_".join(submit.split(' '))
  plot_url = plot2cluster(Hinfo, city)
  df = get_rec(Hinfo, city)
  plot_url = plot2cluster(Hinfo, city)
  return render_template("plot.html", title='test',
                         data=plot_url.resource,
                         htmltable1=df.to_html())


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
