import sqlite3, pygame

conn = sqlite3.connect("Python/revision.db")

conn.execute("""CREATE TABLE SUBJECTS
            (SUBJECT TEXT PRIMARY KEY NOT NULL
            );""")

conn.execute("INSERT INTO SUBJECTS (SUBJECT) \
    VALUES ('Art')")

conn.commit()
conn.close()