import sqlite3, pygame
beingannoying=True

conn = sqlite3.connect("Python/revision.db")
cursorObj = conn.cursor()

subjects = [subject[0] for subject in cursorObj.execute("SELECT SUBJECT FROM SUBJECTS")]

print('which one do you want to add to?')
[print(i+1," ",subjects[i]) for i in range(0,len(subjects))]
while beingannoying:
    try:
        choice = int(input())
    except:
        print('Input an integer')
    else:
        beingannoying=False