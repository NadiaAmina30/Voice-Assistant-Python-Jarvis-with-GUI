import pyttsx3 as p
engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("Hi Nadia, what can i do for you?")
engine.runAndWait()
