from kmeans_hotels import get_clusters
conn = lite.connect("../app.db")
Hinfo = get_clusters()
Hinfo.to_sql('H_normed', conn)
