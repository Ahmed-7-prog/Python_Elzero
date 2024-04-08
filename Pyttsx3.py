import pyttsx3 
engine=pyttsx3.init()


#engine.say("Enter The UserName : ")
UserName=input("Enter The UserName : ")
#engine.runAndWait()

#engine.say("Enter Your Gender Male(M) OR Female(F)")
Gender=input("Enter Your Gender Male(M) OR Female(F):")
#engine.runAndWait()

if Gender=="Male" or Gender=="M":
    engine.say(f"Hello Master:{UserName}")
    engine.runAndWait()
    print(f"Hello Master:{UserName}")

else: #Gender=="Female" or Gender=="F"
    engine.say(f"Hello Miss:{UserName}")
    engine.runAndWait()
    print(f"Hello Miss:{UserName}")


