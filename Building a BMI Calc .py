
Name=input("Enter Your Name : ")
Weight=int(input("Enter Your Weight In Bounds : "))
Height=int(input("Enter Your Height In Inches : "))

BMI=(Weight *703)/(Height**2)

print(BMI)

if BMI>0:
    if BMI<18.5:
        print("Classification : Under Weight\
        HealthRisk : Minimal")
    elif BMI>=18.5 and BMI<=24.9:
        print("Classification : Normal Weight\
        HealthRisk : Minimal")
    elif BMI>=25 and BMI<29.9 :
        print("Classification : Over Weight\
        HealthRisk : Increased")
    elif BMI>=30 and BMI<=34.9 :
        print("Classification : Obese\
        HealthRisk : High")
    elif BMI>=35 and BMI<=39.9 :
        print("Classification : Severely Obese\
        HealthRisk : Very High")
    else :
        print("Classification : Morbidly Obese\
        HealthRisk : Extremely High")
else :
    print("Enter a Valid Input")