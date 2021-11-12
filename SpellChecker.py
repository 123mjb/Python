import spellchecker
from textblob import TextBlob
c = ""
string = input()
list = string.split(" ")
# for a in list:           # incorrect spelling
#    print("original text: "+str(a))
#    b = TextBlob(a)
#    c += str(b.correct()) + " "
#    print("corrected text: "+str(b.correct()))
# print(c)

from spellchecker import SpellChecker
 
spell = SpellChecker()
 
for d in list:
    word = spell.unknown(d)
    print(spell.correction(word))