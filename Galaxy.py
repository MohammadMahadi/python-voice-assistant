import ctypes
import datetime
import os
import random
import smtplib
import subprocess
import time
import webbrowser

import pyjokes
import python_weather
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[1].id) 

# i make speak function for say text voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
    speak("assalamu alaikum") 
    speak("I am Your artificial intelligence My name is Galaxy 1 point 0")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('mrcncvai@gmail.com', '75698560')
    server.sendmail('your email id', to, content)
    server.close()

# make a main method  and than call speak function
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    while True:
         
        query = takeCommand().lower()
        chrome = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        #module function feture
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open_new_tab('https://www.youtube.com')

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open_new_tab("https://google.com")
 
        elif 'open helper' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open_new_tab("https://stackoverflow.com")

        elif 'open facebook' in query:
            speak("Here you go to facebook")
            webbrowser.open_new_tab('https://facebook.com') 
        
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\MAHADI TECHNOLOGY\\Desktop\python practice\\galaxy assistant\\songs"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[random.randint(0,6)]))
        
        elif 'whats time now' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            speak("opening vs code")
            codePath = r"C:\Users\MAHADI TECHNOLOGY\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        
        elif 'open browser' in query:
            speak("opining browser")
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open_new_tab(query)


        elif 'weather' in query:

            client = python_weather.Client(format=python_weather.IMPERIAL)
            weather = client.find("Washington DC")
            speak(weather.current.temperature)

        elif "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif "what is" in query or "who is" in query:
              speak("finding your answers in google")        
              webbrowser.open_new_tab(query)
        
        #asked question awnser here start (not functinal)

        elif "Galaxy" in query:
             
            wishMe()
            speak("Galaxy 1 point o in your service How can I helop you")
        
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Mohammad Mahadi.")
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Gaurav. further It's a secret")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Mohammad Mahadi")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Gaurav ")
            
        elif "i love you" in query:
            speak("It's hard to understand")
