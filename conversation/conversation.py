#!/usr/bin/env python3                                                                                

import os, json
import speech_recognition as sr  

system_language = ""
configured_contexts = []

r = sr.Recognizer()                                                                                   

def runConversation():
    printConversationModeTitle()
    loadConfig()
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
        
        
def loadConfig():
    global system_language
    global configured_contexts

    with open(os.getcwd() + "/config.json") as config_file:
        data = json.load(config_file)
        system_language = data["conversation"]["language"]
        repeat_duration = data["conversation"]["mappings"]
    

def printConversationModeTitle():
    print("#### CONVERSATION MODE ####")