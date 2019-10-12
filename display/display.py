import json, os, time, vlc, sys, thread
from os import listdir
from os.path import isfile, join
from mutagen.mp3 import MP3
from video import runVideoPlayer

audio_path = os.getcwd() + "/display_audio"

audio_file_type = ""
repeat_duration = 0
audio_break = 0
audiofiles = None

audio_thread = None
video_thread = None

def runDisplay():
    printDisplayModeTitle()
    loadConfig()
    loadAudioFiles()
    printConfig()
    startDemoMode()
    
def startDemoMode():
    global video_thread
    global audio_thread
    
    video_thread = thread.start_new_thread(playVideo)
    audio_thread = thread.start_new_thread(playAudio)
    
def playVideo():
    print("Playing Video")

def playAudio():
    time_end = time.time() * 60 * repeat_duration
    fileCount = 0
    while time.time() < time_end:
        if(fileCount + 1 > len(audiofiles)):
            fileCount = 0
        
        current_file_name = audiofiles[fileCount]
        
        if " " in current_file_name:
            current_file_name = renameAudiofile(audio_path, current_file_name)
        
        current_file_path = audio_path + "/" + current_file_name
        
        print("Now Playing: " + current_file_name + "\r")
        
        player = vlc.MediaPlayer(current_file_path)
        player.play()
        
        soundFile = MP3(current_file_path)
        soundDuration = soundFile.info.length
        
        pauseAudioOutput(soundDuration)
        
        fileCount = fileCount + 1
    
    print("Display-Mode finished... Exiting")
    sys.exit()

def loadAudioFiles():
    global audiofiles
    global audio_file_type
    audio_file_type = str(audio_file_type.encode("utf-8"), "utf-8")
    audiofiles = [f for f in listdir(audio_path) if isfile(join(audio_path, f)) and f.endswith(audio_file_type)]

def loadConfig():
    global audio_file_type
    global repeat_duration
    global audio_break

    with open(os.getcwd() + "/config.json") as config_file:
        data = json.load(config_file)
        audio_file_type = data["display"]["audio_format"]
        repeat_duration = data["display"]["repeat_duration"]
        audio_break = data["display"]["audio_break"]

def pauseAudioOutput(currentSoundDuration):
    time.sleep(currentSoundDuration)
    time.sleep(audio_break)

def renameAudiofile(audio_path, filename):
    newName = filename.replace(" ", "_")
    os.rename(audio_path + "/" + filename, audio_path + "/" + newName)
    return newName
    
def printConfig():
    print
    print("############ CONFIG #############")
    print("#\tAudio-Type: " + audio_file_type + "\t#")
    print("#\tRepeat-Duration: " + str(repeat_duration) + "\t#")
    print("#\tAudio-Break: " + str(audio_break) + "\t\t#")
    print("#\tAudio-Files loaded: " + str(len(audiofiles)) + "\t#")
    print("#################################")
    print
     
def printDisplayModeTitle():
    print("#### DISPLAY MODE ####")