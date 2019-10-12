import os, sys

video_config = None
videofiles = None

def runVideoPlayer(videoconfig, videofile_list):
    global video_config
    global videofiles
    
    video_config = videoconfig
    videofiles = videofile_list
    