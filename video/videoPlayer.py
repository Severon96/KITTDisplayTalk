import time, os, sys
from os.path import join, dirname
import cv2

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
        print("No Video-Files loaded... Exiting Video-Playback.")
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
    cap = cv2.VideoCapture(file_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))

    print("This is the fps ", fps)

    if cap.isOpened() == False:
        print("Error File Not Found")

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:

            time.sleep(1 / fps)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def rename_video_file(video_path, filename):
    new_name = filename.replace(" ", "_")
    os.rename(join(video_path, filename), join(video_path, new_name))
    return new_name
