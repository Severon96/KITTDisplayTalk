import playsound, json, os
from os import listdir
from os.path import isfile, join

audio_path = os.getcwd() + "/display_audio"

audio_file_type = ""
repeat_duration = 0
audio_break = 0

audiofiles = None

def runDisplay():
    printDisplayModeTitle()
    loadConfig()
    loadAudioFiles()
    playsound.playsound("test.mp3", True)

def loadAudioFiles():
    global audiofiles
    audiofiles = [f for f in listdir(audio_path) if isfile(join(audio_path, f))]



def loadConfig():
    global audio_file_type
    global repeat_duration
    global audio_break

    data = json.load("config.json")

def printDisplayModeTitle():
    print("#### DISPLAY MODE ####")