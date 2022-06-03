import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import time
import pyjokes
import pyowm
import wikipedia
from googlesearch import search
import subprocess
engine = pyttsx3.init()
voices = engine.getProperty('voices')
c=0
inp=0
while c!='yes':
    print("Select a voice you like:\n"
          "1)David\n"
             "Male\n"
             "English\n")
    engine.setProperty('voice', voices[0].id)
    engine.say("Hello, I'm David. Nice to talk to you.")
    engine.runAndWait()
    print("2)Zira\n"
             "Female\n"
             "English\n")
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello, I'm Zira. Nice to talk to you.")
    engine.runAndWait()
    i=int(input("Enter 1 or 2: "))-1
    if(i==0 or i==1):
        c='yes'
engine.setProperty('voice', voices[i].id)
engine.say("Thank you for choosing me.")
engine.runAndWait()
while inp!="stop":
    inp=input("What would you like me to do sir? ")
    inp=inp.split(" ")
    if(inp[0].lower()=="wikipedia"):
        c=""
        for i in range(1,len(inp)):
            c=c+" "+inp[i]
        print("Searching")
        l=wikipedia.search(c.lstrip(" "))
        for j in range(len(l)):
            print(j,l[j])
        c=int(input())
        r=wikipedia.page(l[c])
        print(r.summary)
        webbrowser.open(r.url)
        #for j in search(c.lstrip(" "),tld="co.in",num=1,stop=1,pause=2):
        #    print(webbrowser.open(j))
            #engine.say(t.summary)
            #engine.runAndWait()
    if (inp[0].lower() == "google"):
        c = ""
        for i in range(1, len(inp)):
            c = c + " " + inp[i]
        print("Searching")
        for j in search(c.lstrip(" "),num=1,stop=1,pause=2):
            print(j)
            webbrowser.open(j)
            try:
                j=str(j[30:])
                c=""
                for i in j:
                    if(i!="_"):
                        c=c+i
                    else:
                        c=c+" "
                r=wikipedia.page(c)
                print(r.summary)
                engine.say(r.summary)
                engine.runAndWait()
            except:
                continue
    if (inp[0].lower() == "open"):
        c = ""
        for i in range(1, len(inp)):
            c = c + " " + inp[i]
        print("Searching for",c.lstrip(" "))
        c="C:\\Users\\ANKIT\\Desktop\\"+c.lstrip(" ")
        #subprocess.Popen([c,'-new-tab'])
        try:
            os.startfile(c)
        except:
            print("I can't find that file. Did you put the right extension?")
            c="C:\\Users\\ANKIT\\Desktop\\"+raw_input("Maybe type the filename with extension: ")
            os.startfile(c)