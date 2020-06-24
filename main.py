# import sqlite3
# import matplotlib

# matplotlib.use('AGG')
# import matplotlib.pyplot as plt
# con = sqlite3.connect("imdb.db")
# con.row_factory = lambda cursor, row: row[0]
# cur = con.cursor()
# director = ('''SELECT director_name FROM movies
#                 where director_name is not ''
#                 group by director_name
#                 order by count(director_name) desc
#                 limit 10''').fetchall()
# movies = cur.execute('''SELECT count(director_name) as films
#                 FROM movies
#                 where director_name is not ''
#                 group by director_name
#                 order by films desc
#                 limit 10''').fetchall()
# con.close()
# fig = plt.figure()
# fig.set_set_size_inches(9,6)
# total = sum(movies)
# plt.pie(movies,(.1,0,0,0,0,0,0,0,0,0),labels = director,
#                                       autopct=lambda p: '{}'.format(int(p * total /100)),
#                                       shadow = True, startangle=90)
# plt.title("Directors with the most movies\nAccording to IMDb")
# # plt.show()
# fig.save_fig(directors.png)
import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
#connect to database file
con = sqlite3.connect("imdb.db")
#gets rid of the tuples that are returned by default
con.row_factory = lambda cursor, row: row[0]
#create cursor object to run queries
cur = con.cursor()
directors = cur.execute('''SELECT director_name
 FROM movies
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
#close the connection
con.close()
fig= plt.figure()
fig.set_size_inches(9,6)
total = sum(movies)
plt.pie(movies,(.1,0,0,0,0,0,0,0,0,0),labels = directors,
 autopct=lambda p: '{}'.format(int(p * total / 100)),
 shadow = True, startangle=90)
plt.title("Directors with the most movies\nAccording to IMDb")
#plt.show()
fig.savefig('directors.png')
