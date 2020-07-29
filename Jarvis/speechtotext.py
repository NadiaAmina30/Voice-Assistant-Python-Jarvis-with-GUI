import speech_recognition as sr
import pyttsx3 as p
r = sr.Recognizer()
engine = p.init()
engine.say("Hi Nadia")
engine.runAndWait()
with sr.Microphone() as source:
    text = r.listen(source)
    
    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")    
    engine.say("What can i do for you?")   
    engine.runAndWait()    
    text1 = r.listen(source)
    
    try:
        recognised_text1 = r.recognize_google(text1)
        print(recognised_text1)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")     