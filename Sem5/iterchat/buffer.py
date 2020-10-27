import sqlite3

tables = '''
PRAGMA foreign_keys = on;
CREATE TABLE IF NOT EXISTS users (
    login TEXT PRIMARY KEY,
    password TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    message TEXT NOT NULL,
    chat_ID INTEGER NOT NULL,
    FOREIGN KEY (chat_ID) REFERENCES chats(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES users(login) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_1 TEXT NOT NULL,
    user_2 TEXT NOT NULL,
    FOREIGN KEY (user_1) REFERENCES users(login) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user_2) REFERENCES users(login) ON UPDATE CASCADE ON DELETE CASCADE
)
'''

con = sqlite3.connect('data.db')
cur = con.cursor()

def create_tables():
    con.execute(tables)
    con.commit()