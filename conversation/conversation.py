#!/usr/bin/env python3                                                                                

import os, json
import speech_recognition as sr  

system_language = ""
configured_contexts = []

r = sr.Recognizer()                                                                                   

def runConversation():
    printConversationModeTitle()
    

def printConversationModeTitle():
    print("#### CONVERSATION MODE ####")