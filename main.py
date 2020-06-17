import sqlite3
import matplotlib

matplotlib.use('AGG')
import matplotlib.pyplot as plt
con = sqlite3.connect("imdb.db")
con.row_factory = lambda cursor, row: row[0]
cur = con.cursor()
data_list1 = cur.execute("QUERY 1").fetchall
data_list2 = cur.execute("QUERY 2").fetchall
director = ('''SELECT director_name FROM movies
                where director_name is not ''
                group by director_name
                order by count(director_name) desc
                limit 10''').fetchall()
movies = cur.execute('''SELECT count(director_name) as films
                FROM movies
                where director_name is not ''
                group by director_name
                order by films desc
                limit 10''').fetchall()
con.close()
fig = plt.figure()
fig.set_set_size_inches(9,6)
total = sum(movies)
plt.pie(movies,(.1,0,0,0,0,0,0,0,0,0))