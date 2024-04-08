#Escape Sequences Characters:

# Back Space \b -->> Escape character and remove it
print("Ahmed\bAkram") #will remove 'd'

#\ Escape new line + Back slash
print("I love\
Ahmed\
AI Engineer") # Escape newline

# by \ we can print " , ' or \ as Back Slash Escape Character

#printing Back Slash by \\
print("The Path is c\\users\\mr\\downloads")

#print single Quotes by \'
print("I love Alphabetic specially \'A\' Character")
print("Ahmed consist of \'A\' , \'h\' , \'m\' , \'e\' & \'d\'")

#print double Quotes by \"
print("I love \"Egypt\"")

#New line or Line Feed by \n
print("I will Write\n This Text\n In New Line")

#Horizontal Tab by \t
print("Ahmed\tAkram")

#Vertical tab by \v
#print("Ahmed\vAkram")

#print the character from hex value by \xhh
print("\x41\x48\x4D\x45\x44 \x41\x4B\x52\x41\x4D") #print AHMED AKRAM

#\r -->>Carriage Return -->>Print after "\r" and remove before it based on the
#Number of characters after "\r"
print("Ahmed\rAkram")#Akram
print("Ahmed\rAkramAmer")#AkramAmer
print("AliadAkram\rAhmed")#AhmedAkram
###############--------------------------------######################