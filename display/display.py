import json, os, time, vlc, sys, _thread
from os import listdir
from os.path import isfile, join
from video.videoPlayer import runVideoPlayer
from audio.audioPlayer import runAudioPlayer
from multiprocessing.dummy import Pool as ThreadPool 

audio_path = os.getcwd() + "/display_audio"

audio_config = {}
video_config = {}

audio_thread = None
video_thread = None

audiofiles = []
videofiles = []

def runDisplay():
    printDisplayModeTitle()
    loadConfig()
    loadAudioFiles()
    printConfig()
    startDemoMode()
    
def startDemoMode():
    global video_thread
    global audio_thread
    
    pool = ThreadPool(2)
    
    video_thread = _thread.start_new_thread(runVideoPlayer, (video_config, videofiles))
    audio_thread = _thread.start_new_thread(runAudioPlayer, (audio_config, audiofiles))
    
def loadAudioFiles():
    global audiofiles
    global audio_config
    audio_file_type = str(audio_config["audio_file_type"].encode("utf-8"), "utf-8")
    audiofiles = [f for f in listdir(audio_path) if isfile(join(audio_path, f)) and f.endswith(audio_file_type)]

def loadConfig():
    global audio_config
    global video_config

    with open(os.getcwd() + "/config.json") as config_file:
        data = json.load(config_file)
        audio_config["audio_file_type"] = data["display"]["audio_format"]
        audio_config["repeat_duration"] = data["display"]["repeat_duration"]
        audio_config["audio_break"] = data["display"]["audio_break"]
        
        video_config["video_file_type"] = data["display"]["video_format"]
    
def printConfig():
    print
    print("############ CONFIG #############")
    print("#\tAudio-Type: " + audio_config["audio_file_type"] + "\t#")
    print("#\tRepeat-Duration: " + str(audio_config["repeat_duration"]) + "\t#")
    print("#\tAudio-Break: " + str(audio_config["audio_break"]) + "\t\t#")
    print("#\tAudio-Files loaded: " + str(len(audiofiles)) + "\t#")
    print("#\tVideo-Files loaded: " + str(len(videofiles)) + "\t#")
    print("#################################")
    print
     
def printDisplayModeTitle():
    print("#### DISPLAY MODE ####")