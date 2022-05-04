import sqlite3, pygame

conn = sqlite3.connect("Python/revision.db")
cursorObj = conn.cursor()

conn.execute("""CREATE TABLE SUBJECTS
            (SUBJECT TEXT PRIMARY KEY NOT NULL
            );""")

conn.execute("INSERT INTO SUBJECTS (SUBJECT) \
    VALUES ('Maths')")
conn.execute("INSERT INTO SUBJECTS (SUBJECT) \
    VALUES ('Geography')")
conn.execute("INSERT INTO SUBJECTS (SUBJECT) \
    VALUES ('History')")
conn.execute("INSERT INTO SUBJECTS (SUBJECT) \
    VALUES ('Art')")



conn.commit()
conn.close()