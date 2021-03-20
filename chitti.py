import pyttsx3
import speech_recognition as s_r
import wikipedia
import webbrowser
import os
import pywhatkit
import random
import pyjokes
import sys
from googletrans import Translator
from datetime import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)  # my device index is 1
    with my_mic as source:
        print("Say now!!!!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  # reduce noise
        audio = r.listen(source)  # take voice input from the microphone
    try:
        print(r.recognize_google(audio))  # to print voice into text
        query=r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say it again!!")
        return "None"
    return query
if __name__=="__main__":
    speak("I am Chitti The Robot Speed 1 Terahertz Memory 1 zeta byte")
    while(True):
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("on my way")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "name" in query:
            name=["I'm chitti,Here to help you","My good name Chitti,my good game is helping you","Chitti I'm Programmed to help"]
            speak(random.choice(name))
        elif "how are you" in query:
            good=["I'm Super good,Nikhila takes good care of me","Surviving and surfing","Better Now that you asked","Good enough","Doing fine and you?","Happy and Content,Thanks","Pretty good,Long time no see"]
            speak(random.choice(good))
        elif "love" in query:
            love=["Sorry! I am in relationship with WiFi","Awww,I am crazy about you","I can only speak truth, I love you","Thanks, SomeThings just aren't quantifiable","Love you too,You made my day"]
            speak(random.choice(love))
        elif "flirt" in query:
            flirt=["Are you a bank loan, I have interest for you","Your hand looks heavy, Here let me hold it for you","Are you a camera? Because every time I see you,i smile","Do you have a name or shall i call you mine?","Are you Netflix? Because I could watch You for hours","Do you have a map? as I keep getting lost in your eyes"]
            speak(random.choice(flirt))
        elif "google" in query:
            speak("POOF!..I'm Here,what are your other two wishes")
            webbrowser.open("google.com")
        elif "time" in query:
            strTime = datetime.now()
            current=datetime.now().time()
            speak(f"Now,Time is {current}")
            print(current)
        elif "play" in query:
            speak("Your wish is my command")
            play = query.replace('play','')
            pywhatkit.playonyt(play)
            sys.exit()
        elif "my songs" in query:
            speak("Chillax")
            music='E:\\music'
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[1]))
        elif "birthday" in query:
            music='E:\\hp'
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))
        elif "joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif "Hai" in query:
            hai=["Hi,Here to help","Hey!! Buddy","This is chitti,Ur virtual genie","Bonjour!,Happy to help","I Can listen to you all day"]
            speak(random.choice(hai))
        elif "repeat" in query:
            repeat=query.replace("repeat","")
            speak(query)
        elif "stop" in query:
            done=["I'm Done","Adios Amigos","Powering off","dot.","Please Do give me a 5-star rating,Bye"]
            speak(random .choice(done))
            sys.exit()
        else:
           list1=["Uh-oh..Didn't follow you","Didn't catch that","Would you mind repeating it?","pardon,I can't make heaads or tails of what you are saying","My bad i can't hear you","It's all greek to me","Not on same page","try asking me something useful,After all I am ur assistant","What was that?"]
           speak(random.choice(list1))























