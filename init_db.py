import sqlite3


connection = sqlite3.connect('database.db')

# инициализируем бд
with open('schema.sql') as db:
    connection.executescript(db.read())

cur = connection.cursor()

cur.execute("INSERT INTO main (id, name, price) VALUES (?, ?, ?)",
            (1, 'Bitcoin', '50000')
            )

cur.execute("INSERT INTO main (id, name, price) VALUES (?, ?, ?)",
            (2, 'Etherium', '7000')
            )


connection.commit()
connection.close()
