import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("database/chrono.db")
cur = conn.cursor()

user = "admin"
password = generate_password_hash("Chrono2026!")

cur.execute(
    "INSERT OR IGNORE INTO users(username,password) VALUES(?,?)",
    (user,password)
)

conn.commit()
conn.close()

print("Administrador creado")
print("Usuario: admin")
print("Clave: Chrono2026!")
