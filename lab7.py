connects = split.connect(users.db)
connects.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)""")

def check_user(user_name, password):
    c.execute("""SELECT * FROM users WHERE username =? AND password =? """, (user_name, password))
    result = c.fetchone():
    if result:
        return True
    else:
        return False

def register():
    user_name = input("Enter a username: ")
    password = input("Enter password: ")