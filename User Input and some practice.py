import math

fname=input('What\'s your first name?')
mname=input('What\'s your middle name?')
lname=input('What\'s your last name?')

#Chain Method
fname=fname.strip().capitalize()
mname=mname.strip().capitalize()
lname=lname.strip().capitalize()

print(f"Hello {fname} {mname:.1s} {lname} , \
Happy To See You!!")

# #Program To Make a Calculator
# #Sum,Subtract,Multiply,Division,Floor Division,Exponentiation
A=int(input("Enter The First Number:"))
B=int(input("Enter The Second Number:"))

Sum=A+B; Subtract=A-B; 

if B==0 :
    print('Division Is Not Allowed , As We Can\'t Divide By Zero')
else:
    print("Division is",A/B)
    print("Floor Divison is",A//B)

Multiply=A*B; Exponentiation=A**B; 

print("Sum is ",Sum)
print("Subtract is ",Subtract)
print("Multiply is ",Multiply)
print("Exponentiation is ",Exponentiation)

# #Program To Calculate The Area Of A Circle

Radius=float(input("Enter The Radius Of a Circle")) 
# PI=3.14

#print("The Area Of a Circle is ", PI*Radius**2 )
print("The Area Of a Circle is ", math.pi*Radius**2)

# #Usage Of Math Library
x=4

y=math.factorial(4) #4*3*2*1
print(y)

y=math.exp(1) # e
print(y)

y=math.sqrt(64)+12 #8+12=20
print(y)

a=int(input())
b=int(input())

if a>b:
    print("if statement is executed")
elif a<b:
    print("elif statement is executed")
else: #a=b
    print("else Statement is executed")

#Program To Determine The Student 's Grade

degree=float(input("Enter Your Degree : "))

if degree>=90 and degree<95 :
    print("Your Grade Is A ")
elif degree>=95 and degree<=100:
    print("Your Grade Is A+")
elif degree>=80 and degree<90:
    print("Your Grade Is B+")
elif degree>=70 and degree>80:
    print("Your Grade Is B")
elif degree>=65 and degree<70:
    print("Your Grade Is C")
elif degree>=55 and degree<65:
    print("Your Grade Is D")
else:
    print("Your Grade Is Failure (Fr)")











