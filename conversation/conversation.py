#!/usr/bin/env python3                                                                                

import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue, json, sys

system_language = ""
configured_contexts = []
device_info = sd.query_devices(kind="input")
q = queue.Queue()


def run_conversation():
    print_conversation_mode_title()
    print(device_info)

    model = Model(lang="de")

    with sd.RawInputStream(samplerate=device_info["default_samplerate"], blocksize=8000, device=device_info["name"],
                           dtype="int16", channels=1, callback=data_handler):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, device_info["default_samplerate"])
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(json.loads(rec.Result())["text"])
                break


def data_handler(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def print_conversation_mode_title():
    print("#### CONVERSATION MODE ####")
