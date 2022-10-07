#!/usr/bin/python

# TODO Create Shell script for Setup!

import sys
import getopt

from display import display
from conversation import conversation

sys.path.insert(1, 'conversation')
sys.path.insert(2, 'display')


def main(argv):
    print_title()

    try:
        opts, args = getopt.getopt(argv, "dc:c")
        if len(opts) == 0:
            print("Please define a mode to start!")
            print("Exiting....")
            sys.exit(1)
            return

        start_modes(opts)
    except getopt.GetoptError as err:
        print(err)
        print('test.py -d (--display) enables Demo-Mode for Displaying KITT')
        # TODO Activate, when implementing the Conversation-Mode
        # print('test.py -c (--conversation) enables Conversation-Mode for talking to KITT')
        sys.exit(2)


def start_modes(opts):
    for opt, arg in opts:
        if opt in ('-d', "--display"):
            print("Entering Displaying-Mode")
            display.run_display()
        # TODO Implement!
        elif opt in ("-c", "--conversation"):
            print("Entering Conversation-Mode")
            conversation.run_conversation()


def print_mode_entering_information(mode_name):
    print("Entering " + mode_name)


def print_title():
    print("#########################################")
    print("#\t\tKITT Display Talk\t#")
    print("# Author:  Dominik Mack\t\t\t#")
    print("# Contact: dominik.mack@icloud.com\t#")
    print("# Version: 0.1a\t\t\t\t#")
    print("#########################################")


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt as e:
        print("User exited")
