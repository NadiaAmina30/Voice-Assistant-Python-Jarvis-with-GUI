import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

import tkinter
from PIL import ImageTk,Image #pip install pillow
from tkinter.constants import YES, BOTH, NW


window = tkinter.Tk()
window.title("Jarvis")
canvas = tkinter.Canvas(window,height=200,width=300)
image = Image.open("C:\\Users\\Nadia Amina\\Downloads\\jarvis.jpg")
resized = image.resize((300,225),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)

canvas.create_image(0,0,image=new_pic,anchor=NW)
canvas.pack(expand=YES,fill=BOTH)

print("Initializing Jarvis")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)  
    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(f"user said:{query}\n")    

    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("Say that again please") 
        query = None
    return query    
def speak(text):
    engine.say(text)
    engine.runAndWait()
    query = takeCommand()
    
    if 'wikipedia' in query.lower():
        try:
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences = 3)
            print(results)
            speak(results)
        except Exception as e:
            speak("Too many results")
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")  
    elif 'what is' in query.lower():
        try:
            
            query = query.replace("what is","")
            results = wikipedia.summary(query,sentences = 3)
            print(results)
            speak(results)
        except Exception as e:
            speak("Too many results")
    elif 'what are' in query.lower():
        try:
            query = query.replace("what are","")
            results = wikipedia.summary(query,sentences = 3)
            print(results)
            speak(results) 
        except Exception as e:
            speak("Too many results") 
    elif 'who is' in query.lower():
        try:
            query = query.replace("what are","")
            results = wikipedia.summary(query,sentences = 3)
            print(results)
            speak(results) 
        except Exception as e:
            speak("Too many results") 
    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'    
        webbrowser.get(chrome_path).open(url)
    elif 'open google' in query.lower():
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'    
        webbrowser.get(chrome_path).open(url)
    elif 'play music' in query.lower():
        songs_dir =b"C:\\Users\\Nadia Amina\\Music\\music" 
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0])) 
    elif 'bye' in query.lower():
        print('Bye')                  

btn1 = tkinter.Button(window,text = "Initialize Jarvis",command = lambda: speak("Initializing.. Jarvis .... How can i help you? "))
btn1.pack()
window.mainloop()    

