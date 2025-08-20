
import pyttsx3

# Read text from Text_Demo.txt
with open('Text_Demo.txt', 'r') as file:
    content = file.read()
    print(content)

# Speak the text
engine = pyttsx3.init()
engine.say(content)
engine.runAndWait()
