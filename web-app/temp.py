from plot2cluster import plot2cluster
from get_table import get_table
import sqlite3 as lite
import pandas as pd

conn = lite.connect('app.db')
Hinfo = pd.read_sql('select * from H_normed', conn)
Hinfo = Hinfo.drop('index', 1)
# cities = pd.read_sql('select * from cities', conn)
plot_url = plot2cluster(Hinfo, 'Ubud_Bali')
# r0, r1 = plot2cluster(Hinfo, 'Ubud_Bali')
# print r0, r1
print get_table(Hinfo, 'New_York_City_New_York')