import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT
)
""")

cursor.execute("INSERT INTO users VALUES (1, 'admin', 'admin123', 'admin@lab.com')")
cursor.execute("INSERT INTO users VALUES (2, 'user', '123456', 'user@lab.com')")

conn.commit()
conn.close()

print("Banco criado com sucesso")
