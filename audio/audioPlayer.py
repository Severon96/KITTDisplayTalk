import time, os, vlc, sys
from mutagen.mp3 import MP3 

audio_path = os.getcwd() + "/display_audio"

audio_config = None

def runAudioPlayer(audioconfig, audiofiles):
    global audio_config
    audio_config = audioconfig
    time_end = time.time() * 60 * audio_config["repeat_duration"]
    fileCount = 0
    
    if(len(audiofiles) == 0):
        print("No Audio-Files loaded... Exiting Audio-Playback.")
        return None
    
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
    
def pauseAudioOutput(currentSoundDuration):
    time.sleep(currentSoundDuration)
    time.sleep(audio_config["audio_break"])

def renameAudiofile(audio_path, filename):
    newName = filename.replace(" ", "_")
    os.rename(audio_path + "/" + filename, audio_path + "/" + newName)
    return newName