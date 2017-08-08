import sqlite3

db = sqlite3.connect('clients.db', check_same_thread=False)
print "Database opened"
db.execute("CREATE TABLE clients (full_name primary key, phone TEXT, email TEXT)")
print "Tables created"
db.close()
