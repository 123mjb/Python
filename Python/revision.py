import sqlite3, pygame
from pygame import *

conn = sqlite3.connect("Python/revision.db")

cursorObj = conn.cursor()

subjects = [subject[0] for subject in cursorObj.execute("SELECT SUBJECT FROM SUBJECTS")]

[print(i+1," ",subjects[i]) for i in range(0,len(subjects))]