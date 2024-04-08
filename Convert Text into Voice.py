import pyttsx3 

engine=pyttsx3.init()

engine.say("What is Your Name ?")
engine.runAndWait()

name=input("What is Your Name ?")

#engine.say("Hello World")
#engine.runAndWait()

engine.say(f"Hello {name}")
engine.runAndWait()
# engine.say(f"Hello {name}")
# engine.runAndWait()

engine.say(" ")
engine.runAndWait()
