import sqlite3, pygame

conn = sqlite3.connect("Python/revision.db")
cursorObj = conn.cursor()

subjects = [subject[0] for subject in cursorObj.execute("SELECT SUBJECT FROM SUBJECTS")]

[conn.execute(f"""CREATE TABLE {subject}
            (QUESTION TEXT PRIMARY KEY NOT NULL,
            Answer TEXT
            );""") for subject in subjects]

conn.commit()
conn.close()