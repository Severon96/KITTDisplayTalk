import playsound, json, os, time, vlc, sys
from os import listdir
from os.path import isfile, join
from mutagen.mp3 import MP3

audio_path = os.getcwd() + "/display_audio"

audio_file_type = ""
repeat_duration = 0
audio_break = 0

audiofiles = None

def runDisplay():
    printDisplayModeTitle()
    loadConfig()
    loadAudioFiles()
    playAudio()

def playAudio():
    time_end = time.time() * 60 * repeat_duration
    fileCount = 0
    while time.time() < time_end:
        if(fileCount + 1 > len(audiofiles)):
            fileCount = 0
        
        current_file_name = audiofiles[fileCount]
        
        print("Now Playing: " + current_file_name + "\r")

        current_file_path = audio_path + "/" + current_file_name
        
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
    audiofiles = [f for f in listdir(audio_path) if isfile(join(audio_path, f)) and f.endswith(".mp3")]

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

def printDisplayModeTitle():
    print("#### DISPLAY MODE ####")