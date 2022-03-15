import sqlite3

from conf import link_to_database, database_name


def start_db():
    global connect_db, cursor_db
    connect_db = sqlite3.connect(link_to_database)
    cursor_db = connect_db.cursor()

    if connect_db:
        print("Database is work.")

    connect_db.execute(f"""CREATE TABLE IF NOT EXISTS {database_name}(
    id INTEGER PRIMARY KEY, 
    user_id INTEGER NOT NULL,
    user_nickname CHAR(20) NOT NULL,
    user_text TEXT NOT NULL,
    predict BOOL NOT NULL
    )
    """)

    connect_db.commit()


def add_info_to_db(user_id: int, user_nickname: str, user_text: str, predict: bool):
    cursor_db.execute(f"""
    INSERT INTO {database_name} (user_id, user_nickname, user_text, predict)
    VALUES (?, ?, ?, ?)
    """, (user_id, user_nickname, user_text, predict))

    connect_db.commit()
