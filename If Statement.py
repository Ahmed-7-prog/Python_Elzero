# Syntax:-
# if boolean :
#    Block Of Code (Be Care With Indentation)

# Assignment 1

# num1=int(input("Enter The First Number:"))
# num2=int(input("Enter The Second Number:"))

# operator=input("Enter The Character To Make Operation (+ OR - OR * OR / OR %)")

# if operator=='+':
#     print(num1+num2)
# elif operator=='-':
#     print(num1-num2)
# elif operator=='*':
#     print(num1*num2)
# elif operator=='/':
#     if num2!=0:
#         print(num1/num2)
#     else:
#         print("As num2 =0 \"ZeroDivisionError\" , We Can\'t divide num1/num2 ")
# elif operator=='%':
#     if num2!=0:
#         print(num1/num2)
#     else:
#         print("As num2 =0 \"ZeroDivisionError\" , We Can\'t Find The Reminder num1%num2 ")
# else:
#     print(f"This Character {operator} not allowed")


# Assignment 2

# age=int(input("Enter Your Age:"))

# print("App Is Suitable For You" if age>16 else "App Is Not Suitable For You")


# # Python program to demonstrate nested ternary operator
# a, b = 10, 20

# print ("Both a and b are equal" if a == b else 
# "a is greater than b"if a > b else "b is greater than a")

# Assignment 3

# age=int(input("Enter Your Age:"))

# print(f"Your Age In Months Is {age*12} Months")
# print(f"Your Age In Weeks Is {age*12*4} Weeks")
# print(f"Your Age In Days Is {age*12*4*7} Days")
# print(f"Your Age In Hours Is {age*12*4*7*24} Hours")
# print(f"Your Age In Minutes Is {age*12*4*7*24*60} Minutes")
# print(f"Your Age In Seconds Is {age*12*4*7*24*60*60} Seconds")

# Assignment 4

# Input Example One "Egypt"
# Input Example Two "Ghana"

# country = input("Input Your Country:").strip().capitalize()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "Oman"]
# price = 100
# discount = 30

# # Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

# if country in countries:
#     print(f"Your Country {country} Eligible For Discount And The Price After Discount Is ${price-discount}")
# else:
#     print(f"Your Country {country} Not Eligible For Discount And The Price Is ${price}")

# CodeForces:V. Comparison

# A=int(input())
# S=input() # Symbol
# B=int(input())


# if S=='>': # A>B
#     print("Right" if A>B else "Wrong")
# elif S=='<': # A<B
#     print("Right" if A<B else "Wrong")
# elif S=='=': # A=B
#     print("Right" if A==B else "Wrong")

# CodeForces: Mathematical Expression 
# A, S, B, Q, C 

# A=int(input())
# S=input() # + OR - OR *
# B=int(input())
# Q=input() # =
# C=int(input())

# if S=='+': # A+B
#     print("Yes" if (A+B==C) else A+B)
# elif S=='-': # A-B
#     print("Yes" if (A-B==C) else A-B)
# elif S=='*': # A*B
#     print("Yes" if (A*B==C) else A*B)


# # Short Hand If Else
# a=10
# b=3
# print("Yes") if(a>b) else print("No")

print("!">"+") # != 33 , + = 43 in ASCII Values


