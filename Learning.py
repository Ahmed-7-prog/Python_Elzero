#indentation
print("Ahmed")
print("Ahmed","Akram",sep="-",end="\t")
print("Ahmed","Akram","Amer",sep="-",end="\t")
age=5
print(age)

#Variales
#int float string bool list tuple dict set
#type() -->>Built-in Function Show The DataType Of a Variable
########################---------------------------------#################

#Escape Sequences Characters:

# Back Space \b -->> Escape character and remove it
print("Ahmed\bAkram") #will remove 'd'

#\ Escape new line + Back slash
print("I love\
Ahmed\
AI Engineer") # Escape newline

# by \ we can print " ' or \ as Back Slash Escape Character

#printing Back Slash by \\
print("The Path is C:\\users\\mr\\downloads")

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
print("Ahmed\vAkram")

#print the character from hex value by \xhh (Hex Decimal)
print("\x41\x48\x4D\x45\x44 \x41\x4B\x52\x41\x4D") #print AHMED AKRAM

#\r -->>Carriage Return -->>Print after "\r" and remove before it based on the
#Number of characters after "\r"
print("Ahmed\rAkram")#Akram
print("Ahmed\rAkramAmer")#AkramAmer
print("AliadAkram\rAhmed")#AhmedAkram
###############--------------------------------######################


#Concatenation between Strings not Numbers

A="I Love"
B="Python"
print(A+"\n"+B)
print(A+"\t"+B) # or print(A+" "+B)

C=A+" "+B
print(C)

D="My\
hope\
to\
be a\
good man"

E="I\
also\
hope to\
be a\
AI Engineer"

print(D+","+E)

# No concatenation with a number
#print("Hello"+10) can only concatenate str (not "int") to str

#Strings
#the text value may be in single or double quotes
MyStringone='This is Single Quote'
MyStringtwo="This is double Quotes"

print(MyStringone)
print(MyStringtwo)

#you can put " " in '  ' and vice-versa
MyStringthree='U Can Print Double Quotes inside Single Quote"Test"'
MyStringfour="U Can Print single Quote inside Double Quotes'Test'"

print(MyStringthree)
print(MyStringfour)
#Usage of Trible Double Quotes""" """ or Trible Single Quote''' '''
#and we can print single or double quotes in them
MyStringfive="""I Learn
Strings \
Lesson \\\With Osama "Test" 'Test'
ElZero
"""
# Observe The Difference between \ in one end and inside text
MyStringsix="""I Learn
Strings                         
Lesson With\\\ Osama "Test" 'Test'\
ElZero
"""
print(MyStringfive)
print(MyStringsix)
##################----------------------------#######################

#Conversion by built-in functions str(),int(),float(),bool():
    # to string str(--)
    # to int int(--)
    # to float float(--)
    # to bool bool(--)
Age=25
print("Hello,Iam "+str(Age)+" old" )
conv_int="1234"
print(int(conv_int))

conv_float="123.4"
print(float(conv_float))

conv_bool="0"
print(bool(conv_bool)) #Always o/p=True
###################--------------------------------####################

#Indexing & Slicing:
My_String="I Love Python"

# Indexing
# Syntax: [Index] -->> Index start from zero(zero-base)
print(My_String[0]) #O/P= first Character by +ve Index 'I'
print(My_String[-13]) #O/P= first Character by -ve Index 'I'
print(My_String[12]) #O/P= first Character by -ve Index 'n'
print(My_String[-1]) #O/P= first Character by -ve Index 'n'


#Slicing

#Syntax: [start:end]
#Syntax: [start:end:steps]
#End Not  Included
print(My_String[0:5]) #O/P= from index=0 to index=end-1 as end not included.
# o/p= I Lov
print(My_String[:5]) #Will Start From index=0

print(My_String[0:]) #Will go to the end
print(My_String[:]) #O/P= first Character by -ve Index 'n'

#Second Syntax [start:end:steps]
#if steps=n it will skip n-1 characters
print(My_String[4:6:1]) # skip 1-1=0 NO chracter
print(My_String[::2]) # skip 2-1=1 character
#####################-----------------------------------#####################


#String Method Lesson 1
# We Have Some Built-in Functions : len(),strip(),rstrip(),lstrip()
# capitalize(),title(),zfill(),lower(),upper()

s="Five"
print(len(s)) #return The Number of Characters of a string o/p=4
print(len("Ahmed Akram")) #o/p=11

print("Ahmed"*2) # Will Repeat "Ahmed" Twice
print("Pyyhon is Pretty "*3) # Will Repeat "Python is Pretty" Third

#1- strip() ,rstrip()& lstrip() -->> Remove Characters but not in middle
s="    Python    "
print(s.strip()) #O/P=Python
print(s.rstrip()) #O/P=    Python 
print(s.lstrip())# O/P=Python

#If We Want To Remove a Special Character
s="PPythonPPppp"
print(s.strip("#"))
print(s.rstrip("#"))
print(s.lstrip("#"))
print(s.strip("P"))

#2-title() & captialize()
s=" 3d animiation by ahmed akram"
print(s.title())
r="ahmed akram is a data analyist"
print(r.capitalize())
print(r.title())

#3- upper() & lower()

r="swimming"
print(r.upper())
r="AHMED"
print(r.lower())
###############________________________________________####################

#String Methods 2

#1-split()

d="I Love Python PhP and MySql"
print(d.split())
d="I-Love-Python-PhP-and-MySql"
print(d.split("-"))
print(d.split())

#split(Separator,MaxSplit)
a="I-Love-Python-PhP-and-MySql"
print(a.split("-",2))
print(a.split("-",3))

#2-rsplit()
print(a.rsplit("-",3))

#Usage of " in " KeyWord
a="Ahmed Akram"
print("hm"in a) # will return True or False
print("Hm"in a) 
print(" "in a) 
print("Ahmed"in a) 

if("Ahmed"in a):
    print("True")

print(type("Ahmed"in a)) # This Type is bool that return True or False

#Usage of "not in" KeyWord
b="Kamel Amer"
print("Ka" not in b) # if not in return True , otherwise return False 
print("KA" not in b) 

if("Ar" not in b):
    print("True It is not in a string")

#replace() -->>Built-in functions: replace
c="Python awesome!"
print(c.replace("Python","C++"))
d="Ahmed Akram"
print(d.replace('A','K'))
#if character is repeated ,will remove all of it

#Usage of Format Function by aid of {} to Place Number in The Right Place
Age=20
print("I am Ahmed Akram , I am {} ".format(Age))

price=40
numbers=5
product=567
print("I bought {0} with {1} numbers with price {2}".format(product,numbers,price))

#\000 usage of Octal Value Same As \xhh Hex Value
print("\123\110\101\111\115\101\101 \115\117\110\101\115\115\105\104")
#\f -->>Form Feed
print("\fAhmed\fAkram\f")

#expandtabs()
f="Ahmed\tAkram\tWith\tZeyad\tAkram"
print(f.expandtabs(3)) #Control The Number Of Spaces

#To Check String is....
one="I Love Python And 3D"
two="I Love Python And 3d"
# istitle()-->>Check if the string is title or not
print(one.istitle())
print(two.istitle())

three=" "
four=""
#isspace()-->> Check if the string cotain spaces or not
print(three.isspace())
print(four.isspace())

five="ahmed akram"
fiveMod="Ahmed Akram"
#islower()-->>Check if all characters is in LowerCase or not
print(five.islower())
print(fiveMod.islower())
six="AHMED AKRAM"
sixMod="AHmeD AkraM"
#isupper()-->>Check if all characters is in UpperCase or not
print(six.isupper())
print(sixMod.isupper())


# Operators
#1-Arthihmetic: Addition-Subtraction-Multiplication-Division-Exponentation-FloorDivision

print(-30- -20)
print(100/50)# Result Is Floating Point Number
print(int(100/50))# By int()-->>Result Will Be Integer as Integer Division

# if num%2=0 -->>num:even else num:odd so num%2!=0 but Equal 1
print( 20 % 2 ) #20 is even 
print( 21 % 2 ) #21 is odd 

# Modulus By 10 -->>Return first Digit
print( 23 % 10 ) # Return 3
# Modulus By 100 -->>Return first Two Digit
print( 123 % 100 ) # Return 23
# Modulus By 1000 -->>Return first Three Digit
print( 1423 % 1000 ) # Return 3
# And So On

#Precedence
print(1+5/2*2) # 6.0
print((1+5)/(2*2)) # 1.5

#Expnonentation-->>Power
print(5**2) # 5*5=25

#FloorDivision
print(11//2) #5.5-->>5
print(13//2) #6.5-->>6

print("#"*50)

# Boolean
# False Values
print(bool(0))
print(bool("")) # Empty String
print(bool('')) # Empty String
print(bool(False))
print(bool({})) # Empty Dictionary
print(bool(())) # Empty Tuple
print(bool([])) # Empty List
print(bool(None))
print("++"*10) # Separator
# True Values
print(bool(True))
print(bool("Ahmed"))
print(bool(" "))
print(bool(110))
print(bool(110.234))
print(bool(-11120.33))
print(bool([1,2,3])) # List
print(bool((1,2,3))) # Tuple
print(bool({1,2,3})) # Dictionary

print("++"*10)

# Boolean Operations
# Boolean Multiplication
print(True*True) # 1*1=1
print(True*False) # 1*0=0 
print(False*False) # 0*0=0

# Boolean Addition
print(True+True) # 1+1=2
print(True+False) # 1+0=1
print(False+False) #0+0=0

# Boolean Subtraction
print(False-False) #0-0=0
print(False-True) #0+1=-1
print(True-False) #1-0=1
print(True-True) #1-1=0

# Boolean Division
# print(False/False) #0/0 -->> Can't Divide By Zero 
# print(True/False) #1/0  -->> Can't Divide By Zero
print(True/True) #1/1=1.0
print(False/True) #0/1=0.0

# Boolean Operators : and -or -not

print(not True) #False
print(not False) #True
print(not 10<6) # False--->True
print(not 10>5) #True--->False

print(10>5 and 11<15 ) # True
print(10>5 or 11>15 ) # True
print("="*50)

#Format By Old Way
#%s-->>String 
#%d-->>Integer
#%f-->>Floating Point Number

#To Control Floating Point -->> By %._f 
#To Truncate String -->> By %._s 

str1="Ahmed"
age1=20
rank=10

print("My Name Is %s"%str1)
print("My Age Is %s"%age1)
print("My Rank Is %s"%rank)
print("I am %.5s and My Age is %d and My Rank is %.3f" %( str1 ,age1 , rank ))

#Format By New Way
#{:s}-->>String
#{:d}-->>Integer Number
#{:f}-->>Floating Point Number
#Using ".format(-,-,-,...)"
str1="Ahmed"
age1=20
rank=10

print("I am {}".format(str1))
print("I am {} Years Old".format(age1))
print("My Rank Is {}".format(rank))
print("I am {} , I am {} Years Old And My Rank Is {}".format(str1,age1,rank))
print("I am {:s} ,I am {:d} Years Old And My Rank Is {:f}".format(str1,age1,rank))

#To ConTrol Floating Point By {:._f}
print("I am {:s} , I am {:d} Years Old And My Rank Is {:.2f}".format(str1,age1,rank))

#Truncate String By {:_s}
name="Hello Ahmed Amer"
print("My Message is {}".format(name))
print("My Message is {:s}".format(name))
print("My Message is {:.11s}".format(name))

# Foramtting Numbers
#{:"Char That I Want To Put Between Numbers" d}
salary=2000
print("My Salary Is {}".format(salary))
print("My Salary Is {:d}".format(salary))
print("My Salary Is {:_d}".format(salary))
print("My Salary Is {:,d}".format(salary))

#ReArranging Items (String,Numbers)

#Data-->>Objects: Zero-Based Indexing In Python

#Examble
a,b,c="Ahmed","Akram","Zeyad"
print("Hello {} {} {}".format(a,b,c)) #a-->>0 ,b-->>1,c-->>2
print("Hello {1} {2} {0}".format(a,b,c))

x,y,z=10,20,30
print("Numbers : {} {} {}".format(x,y,z)) #x-->>0 ,y-->>1,z-->>2
print("Numbers : {2} {1} {0}".format(x,y,z))
print("Numbers : {2:d} {1:d} {0:d}".format(x,y,z))
print("Numbers : {2:.2f} {1:.3f} {0:.4f}".format(x,y,z))

#Anthor Wonderful Way For Formatting
print(f"Numbers : {x} {y} {z}")

print("="*50)
print("Tammmmmmmmmmmam")













