print("What is your name?")
Name = input()
NameFile = Name + ".txt"
print (NameFile)
file = open(NameFile, "w")
file.write("Hello")
print(file)
file.close()