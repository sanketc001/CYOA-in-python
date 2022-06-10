import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import time
import pyjokes
import pyowm
from PyDictionary import PyDictionary
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
def weather():
    v=pyowm.OWM()
    ob=v.weather_at_place("London,uk")
    c=ob.get_weather()
    print(c.get_wind())
weather()
d=PyDictionary()
print(d.values())
print(os.path.abspath("C:\\Users\\ANKIT\\Desktop"))
listener = sr.Recognizer()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
c=0
while c!='yes':
    print("Select a voice you like:\n"
          "1)David\n"
             "Male\n"
             "English\n")
    engine.setProperty('voice', voices[0].id)
    engine.say("Hello, I'm David. Nice to meet you.")
    engine.runAndWait()
    print("2)Zira\n"
             "Female\n"
             "English\n")
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello, I'm Zira. Nice to meet you.")
    engine.runAndWait()
    i=int(input("Enter 1 or 2: "))-1
    if(i==0 or i==1):
        c='yes'
engine.setProperty('voice', voices[i].id)
talk(r.recognize_google(audio))











'''

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()'''