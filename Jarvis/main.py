import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#function will make Jarvis speak the string passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
#function will take command from microphone
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

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("email@gmail@gmail.com",to,content)
    server.close()
speak("Initializing.. Jarvis .... How can i help you? ")    
query = takeCommand()
#Main program
if 'wikipedia' in query.lower():
    try:
        speak('Searching wikipedia')
        query = query.replace("Wikipedia","")
        results = wikipedia.summary(query,sentences = 3)
        print(results)
        speak(results)
    except Exception as e:
        print(e)  
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")                   
elif 'what is' in query.lower():
    try:
        speak('Searching wikipedia')
        query = query.replace("what is","")
        results = wikipedia.summary(query,sentences = 3)
        print(results)
        speak(results)
    except Exception as e:
        print(e)    
elif 'what are' in query.lower():
    try:
        speak('Searching wikipedia')
        query = query.replace("what are","")
        results = wikipedia.summary(query,sentences = 3)
        print(results)
        speak(results) 
    except Exception as e:
        print(e)
elif 'who is' in query.lower():
    try:
        speak('Searching wikipedia')
        query = query.replace("what are","")
        results = wikipedia.summary(query,sentences = 3)
        print(results)
        speak(results) 
    except Exception as e:
        print(e)               
      
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
elif 'email' in query.lower():
    try:
        speak("What should i send")
        content = takeCommand()
        to = "email@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent successfully")
    except Exception as e:
        print(e)    
