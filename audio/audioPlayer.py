import time, os, sys
from os.path import join, dirname

from mutagen.mp3 import MP3
from playsound import playsound

audio_path = join(dirname(dirname(__file__)), "display_audio")

audio_config = None


def run_audio_player(audioconfig, audiofiles):
    global audio_config
    audio_config = audioconfig
    time_end = time.time() * 60 * audio_config["repeat_duration"]
    file_count = 0

    if len(audiofiles) == 0:
        print("No Audio-Files loaded... Exiting Audio-Playback.")
        return None

    while time.time() < time_end:
        if file_count + 1 > len(audiofiles):
            file_count = 0

        current_file_name = audiofiles[file_count]

        if " " in current_file_name:
            current_file_name = rename_audio_file(audio_path, current_file_name)

        current_file_path = join(audio_path, current_file_name)

        print("Now Playing: " + current_file_name + "\r")

        playsound(current_file_path)

        sound_file = MP3(current_file_path)

        file_count = file_count + 1

    print("Display-Mode finished... Exiting")
    sys.exit()


def parse_audio_output(current_sound_duration):
    time.sleep(current_sound_duration)
    time.sleep(audio_config["audio_break"])


def rename_audio_file(audio_path, filename):
    new_name = filename.replace(" ", "_")
    os.rename(join(audio_path, filename), join(audio_path, new_name))
    return new_name
