import json
from os import listdir
from os.path import isfile, join, dirname
from video.videoPlayer import run_video_player
from audio.audioPlayer import run_audio_player

audio_path = join(dirname(dirname(__file__)), "display_audio")
video_path = join(dirname(dirname(__file__)), "videofiles")

audio_config = {}
video_config = {}

audio_thread = None
video_thread = None

audio_files = []
video_files = []


def run_display():
    print_display_mode_title()
    load_config()
    load_audio_files()
    load_video_files()
    print_config()
    start_demo_mode()


def start_demo_mode():
    # Commented out, since it's not yet supported
    run_video_player(video_config, video_files)
    run_audio_player(audio_config, audio_files)


def load_audio_files():
    global audio_files
    global audio_config
    audio_file_type = str(audio_config["audio_file_type"].encode("utf-8"), "utf-8")
    audio_files = [audio_file for audio_file in listdir(audio_path) if isfile(join(audio_path, audio_file)) and audio_file.endswith(audio_file_type)]


def load_video_files():
    global video_files
    global video_config
    video_file_type = str(video_config["video_file_type"].encode("utf-8"), "utf-8")
    video_files = [video_file for video_file in listdir(video_path) if isfile(join(video_path, video_file)) and video_file.endswith(video_file_type)]


def load_config():
    global audio_config
    global video_config

    with open(join(dirname(dirname(__file__)), "config.json")) as config_file:
        data = json.load(config_file)
        audio_config["audio_file_type"] = data["display"]["audio_format"]
        audio_config["repeat_duration"] = data["display"]["repeat_duration"]
        audio_config["audio_break"] = data["display"]["audio_break"]

        video_config["video_file_type"] = data["display"]["video_format"]
        video_config["repeat_duration"] = data["display"]["repeat_duration"]


def print_config():
    print
    print("############ CONFIG #############")
    print("#\tAudio-Type: " + audio_config["audio_file_type"] + "\t#")
    print("#\tRepeat-Duration: " + str(audio_config["repeat_duration"]) + "\t#")
    print("#\tAudio-Break: " + str(audio_config["audio_break"]) + "\t\t#")
    print("#\tAudio-Files loaded: " + str(len(audio_files)) + "\t#")
    print("#\tVideo-Files loaded: " + str(len(video_files)) + "\t#")
    print("#################################")
    print


def print_display_mode_title():
    print("#### DISPLAY MODE ####")
