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
print(bool({1,2,3})) # Set

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