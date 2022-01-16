import sqlite3 as sql

conection = sql.connect('newDB.sqlite')
q = conection.cursor()

# q.execute('''CREATE TABLE user2 (id int auto_increment primary key, name varchar, pass varchar)''')
# conection.commit()

user_name = "Alex"
user_pass = "12345"

q.execute("INSERT INTO user (name, pass) VALUES ('%s', '%s')"%(user_name, user_pass))
conection.commit()

print("Users:\n")

q.execute("SELECT * FROM user")
row = q.fetchone()

while row is not None:
    print("Name:", row[1], "Pass:", row[2])
    row = q.fetchone()

# Close DB
q.close()
conection.close()
