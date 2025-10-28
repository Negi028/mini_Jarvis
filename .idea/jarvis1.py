import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'chinku' in command:
               print(command)
    except:
        pass
    return command

def run_chinku():
    command = takeCommand()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)

    elif 'who the heck is ' in command:
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)

while True:
    run_chinku()
