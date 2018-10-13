from pyArango.connection import *

conn = Connection(username='root', password='1111')
db = conn.createDatabase(name='Logs')

db = conn['Logs']

allLogs = db.createCollection(name="all")
loginLogs = db.createCollection(name="login")
logoutLogs = db.createCollection(name="logout")
registerLogs = db.createCollection(name="register")
moviesearchLogs = db.createCollection(name="movie_search")
humansearchLogs = db.createCollection(name="human_search")
subscriptions = db.createCollection(name="subscriptions")