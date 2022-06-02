import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import time
import pyjokes
import randfacts
from googlesearch import search
import wikipedia
import requests
import pywhatkit
import smtplib
from datetime import datetime as dt
import tkinter as tk
import cv2
import pyautogui
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
import googlemaps
from datetime import datetime
import PIL.Image
def asciiart():
    # path=input("Enter valid path to image: ")
    path = "Newstudent001.jpg"
    try:
        img = PIL.Image.open(path)
    except:
        print("Invlid path")
    asciichars="@ # $ % ? * + ; : , .".split(" ")
    print(asciichars)
    w,h=img.resize((800,600)).size
    r=h/w
    nh=int(100*r)
    print(w,h,10,nh,r)
    img=img.resize((100,nh))
    img=img.convert("L")
    pix=img.getdata()
    ch="".join([asciichars[pixel//25] for pixel in pix])
    pixc=len(ch)
    asciiimg="\n".join(ch[i:(i+100)] for i in range(pixc))
    print(asciiimg)
#asciiart()
def mapping():
    gmaps = googlemaps.Client(key='AIzaSyCR1YVndr9SfMY9KFpneIhbiet2QEGrVCo')
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall","Parramatta, NSW",mode="transit",departure_time=now)
    for step in directions_result['Directions']['Routes'][0]['Steps']:
        print(step['descriptionHtml'])
def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB,multichannel=True)
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    plt.show()
def facerec():
    vid = cv2.VideoCapture(0)
    while True:
        ret, image = vid.read()
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"/haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=5,minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            image=image[y-10:y+h+10,x-10:x+w+10]
        try:
            cv2.imshow('faces', image)
        except:
            pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("Newstudent002.jpg",image)
            compare_images(cv2.imread("Newstudent001.jpg"),cv2.resize(cv2.imread("Newstudent002.jpg"),(311,311)),"Matching")
            break
    vid.release()
    cv2.destroyAllWindows()
def webcam():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
def screenshot():
    resolution = (1920,1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "Recording.avi"
    fps = 120.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 1000, 720)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        frame=frame
        cv2.imshow('Live', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
window = tk.Tk()
r=sr.Recognizer()
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
    inp=''
    try:
        with sr.Microphone() as source:
            print("What would you like me to do sir?")
            engine.say("What would you like me to do sir? ")
            engine.runAndWait()
            audio = r.listen(source,phrase_time_limit=5)
            inp=r.recognize_google(audio)
    except:
        time.sleep(5)

    inp=inp.split(" ")
    if(inp[0].lower()=="wikipedia"):
        c=""
        for i in range(1,len(inp)):
            c=c+" "+inp[i]
            a = tk.Label(text="Searching sir!")
            a.pack()
            window.mainloop()
        engine.say('Searching sir!')
        engine.runAndWait()
        l=wikipedia.search(c.lstrip(" "))
        for j in range(len(l)):
            print (j,l[j])
        c=int(input())
        r=wikipedia.page(l[c])
        print (r.summary)
        webbrowser.open(r.url)
        #for j in search(c.lstrip(" "),tld="co.in",num=1,stop=1,pause=2):
        #    print webbrowser.open(j)
            #engine.say(t.summary)
            #engine.runAndWait()

    if (inp[0].lower() == "google"):
        c = ""
        for i in range(1, len(inp)):
            c = c + " " + inp[i]
        a1 = tk.Label(text="Searching")
        a1.pack()
        window.mainloop()
        for j in search(c.lstrip(" "),num=1,stop=1,pause=2):
            print (j)
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
                print (r.summary)
                engine.say(r.summary)
                engine.runAndWait()
            except:
                continue
    if (inp[0].lower() == "open"):
        c = ""
        for i in range(1, len(inp)):
            c = c + " " + inp[i]
            a2 = tk.Label(text="Searching sir!")
            a2.pack()
            window.mainloop()
            print(a2,c.lstrip(" "))
        c="C:\\Users\\toshe\\OneDrive\\Desktop\\"+c.lstrip(" ")

        try:
            for i in ['.jpg','.exe','.jpeg','.png','.pdf','.docx','.pptx']:
                if os.path.exists(c+i):
                    os.startfile(c+i)

        except:
            print ("I can't find that file. Did you put the right extension?")
            c="C:\\Users\\toshe\\OneDrive\\Desktop\\"+input("Maybe type the filename with extension: ")
            os.startfile(c)

      # WEATHER

    if (inp[0].lower() == "weather"):
        with sr.Microphone() as source:
            a3 = tk.Label(text='Which city\'s weather would you like to know sir?')
            a3.pack()
            window.mainloop()
            engine.say("Which city's weather would you like to know sir?")
            engine.runAndWait()
            audio = r.listen(source,phrase_time_limit=5)
            city_name=r.recognize_google(audio)

            # Enter your API key here
            api_key = '313fc6e74e0f9ae6a92dfb9daf6a5123'

            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            # Give city name

            # complete_url variable to store
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            # get method of requests module
            # return response object
            response = requests.get(complete_url)

            # convert json format data into
            # python format data
            x = response.json()
            print(x)
            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"] != "404":
                # store the value of "main"
                # key in variable y
                y = x["main"]

                # store the value corresponding
                # to the "temp" key of y
                current_temperature = y["temp"]

                # store the value corresponding
                # to the "pressure" key of y
                current_pressure = y["pressure"]

                # store the value corresponding
                # to the "humidity" key of y
                current_humidiy = y["humidity"]

                # store the value of "weather"
                # key in variable z
                z = x["weather"]

                # store the value corresponding
                # to the "description" key at
                # the 0th index of z
                weather_description = z[0]["description"]

                # print following values
                print(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            if weather_description.lower() in ['mist', 'smoke', 'haze', 'fog']:
                a4 = tk.Label(text="Stay focused on the road. Driving in fog is not a time for multi-tasking.")
                a4.pack()
                window.mainloop()
                engine.say("Stay focused, Driving in fog is not a time for multi-tasking sir")
                engine.runAndWait()

            if weather_description.lower() in ['rain', 'light rain', 'moderate rain', 'heavy intensity rain',
                                               'very heavy rain', 'extreme rain', 'freezing rain',
                                               'light intensity shower rain', 'shower rain',
                                               'heavy intensity shower rain', 'ragged shower rain']:
                a5= tk.Label(text="You may want to carry your umbrella.")
                a5.pack()
                window.mainloop()
                engine.say('You may want to carry your Umbrella sir')
                engine.runAndWait()

            if weather_description.lower() in ['clear sky', 'Clear']:
                a6 = tk.Label(text="You can have a sun bath today.")
                a6.pack()
                window.mainloop()
                engine.say('You can have a sun bath,sir')
                engine.runAndWait()

            if weather_description.lower() in ['thunderstorm', 'thunderstorm with light rain', 'thunderstorm with rain',
                                               'thunderstorm with heavy rain', 'light thunderstorm', 'thunderstorm',
                                               'heavy thunderstorm', 'ragged thunderstorm',
                                               'thunderstorm with light drizzle', 'thunderstorm with drizzle',
                                               'thunderstorm with heavy drizzle']:
                a7 = tk.Label(text='Stay at home or you will fly up and away')
                a7.pack()
                window.mainloop()
                engine.say('Stay at home or you will fly up up and away, sir ')
                engine.runAndWait()

            if weather_description.lower() in ['snow', 'light snow', 'heavy snow', 'light shower sleet', 'shower sleet',
                                               'light rain and snow', 'rain and snow', 'light shower snow',
                                               'shower snow', 'heavy shower snow']:
                a8 = tk.Label(text='You may need to dig out your car from snow')
                a8.pack()
                window.mainloop()
                engine.say('You may need to dig out your car from snow')
                engine.runAndWait()

            if weather_description.lower() in ['clouds', 'few clouds', 'scattered clouds', 'broken clouds',
                                               'overcast clouds']:
                a9 = tk.Label(text='Somewhere shady somewhere light')
                a9.pack()
                window.mainloop()
                engine.say('Somewhere shady somewhere light')
                engine.runAndWait()

    if (inp[0].lower() == "fact"):
        b = tk.Label(text='Here is a random facts')
        b.pack()
        window.mainloop()
        engine.say("Here is a random facts")
        engine.runAndWait()
        x = randfacts.getFact(True)
        print(x)
        engine.say(x)
        engine.runAndWait()

    if (inp[0].lower() == "joke"):
        b1 = tk.Label(text='Here is a joke for you!')
        b1.pack()
        window.mainloop()
        engine.say("Here is a joke for you!")
        engine.runAndWait()
        j = pyjokes.get_joke(language='en', category='neutral')
        print(j)
        engine.say(j)
        engine.runAndWait()

    if (inp[0].lower() == "youtube"):
        b2 = tk.Label(text='opening youtube . . .')
        b2.pack()
        window.mainloop()
        engine.say('opening youtube')
        engine.runAndWait()
        b3 = tk.Label(text='what would you like me to play sir?')
        b3.pack()
        window.mainloop()
        engine.say('what would you like me to play sir?')
        engine.runAndWait()

        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=5)
            try:
                str1 = r.recognize_google(audio)
                engine.say(str1)
                engine.runAndWait()
            except:
                b4 = tk.Label(text="some error occurred!")
                b4.pack()
                window.mainloop()
                engine.say('some error occurred')
                engine.runAndWait()



        query = str1+' youtube'
        for j in search(query, tld="co.in", num=10, stop=1, pause=0.25):
            print(j)
        webbrowser.open_new(j)

            #####Whatsapp

    if (inp[0].lower() == 'whatsapp'):
        b5 = tk.Label(text='opening whatsapp')
        b5.pack()
        window.mainloop()
        engine.say('opening whatsapp')
        engine.runAndWait()


        contacts = {"Sanket": "+918910904108", "Shivam": "+918804749141", "Rishab": "+918483942099",
                    "Tosheet": "+919370626140", "Sidhant": "+917325927812","Sulaxan Sir": "+917350819867"}

        for i in contacts.keys():
            print(i)
        engine.say('Whom would you like to send message to sir?')
        name = input('Whom would you like to send message to, sir?')

        a = int(str(dt.now())[11:13])
        b = int(str(dt.now())[14:16])+1

        pywhatkit.sendwhatmsg(contacts[name],"Jarvis here! This is an Expert System Conversational Chatbot created by STRTRS. Please do not reply!",a,b,wait_time=5)
        b += 1



            ##Mail

    if (inp[0].lower() == 'mail'):

        sen_email_id = ("JarvisESBOT@gmail.com")
        message = " Jarvis here! This is an Expert System Conversational Chatbot created by STRTRS. Please do not reply!"

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login("JarvisESBOT@gmail.com", 'Jarvis23557')
        mailid = input('Who would you like to send a message')
        s.sendmail("JarvisESBOT@gmail.com", mailid, message)

        b6 = tk.Label(text='Email Sent')
        b6.pack()
        window.mainloop()