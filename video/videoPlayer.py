import time, os, sys
from os.path import join, dirname
import cv2

from playsound import playsound

video_config = None
videofiles = None

video_path = join(dirname(dirname(__file__)), "videofiles")


def run_video_player(videoconfig, videofile_list):
    global video_config
    global videofiles
    time_end = time.time() * 60 * videoconfig["repeat_duration"]
    file_count = 0

    video_config = videoconfig
    videofiles = videofile_list

    print(video_config)
    print(videofile_list)

    if len(videofiles) == 0:
        print("No Audio-Files loaded... Exiting Audio-Playback.")
        return None

    while time.time() < time_end:
        if file_count + 1 > len(videofiles):
            file_count = 0

        current_file_name = videofiles[file_count]

        if " " in current_file_name:
            print("spaced")
            current_file_name = rename_video_file(video_path, current_file_name)
            videofiles[file_count] = current_file_name

        current_file_path = join(video_path, current_file_name)

        print("Now Playing: " + current_file_name + "\r")

        play_video(current_file_path)

        file_count = file_count + 1

    print("Display-Mode finished... Exiting")
    sys.exit()


def play_video(file_path):
    video = cv2.VideoCapture(file_path)

def rename_video_file(video_path, filename):
    new_name = filename.replace(" ", "_")
    os.rename(join(video_path, filename), join(video_path, new_name))
    return new_name
