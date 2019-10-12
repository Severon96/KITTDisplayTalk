#!/usr/bin/env python3                                                                                

import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   


def runConversation():
    print("#### CONVERSATION MODE ####")
    startSpeechrecognition()
    
def startSpeechrecognition():
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        print("You said " + r.recognize_google(audio, language="de-DE"))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))    