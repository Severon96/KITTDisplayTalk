#!/usr/bin/python

#TODO Create Shell script for Setup!

import sys
import getopt
sys.path.insert(1, 'conversation')
sys.path.insert(2, 'display')
from display import runDisplay
from conversation import runConversation

def main(argv):
    printTitle()
    try:
        opts, args = getopt.getopt(argv, "dc:")
    except getopt.GetoptError as err:
        print(err)
        print('test.py -d (--display) enables Demo-Mode for Displaying KITT')
        #TODO Activate, when implementing the Conversation-Mode
        #print('test.py -c (--conversation) enables Conversation-Mode for talking to KITT')
        sys.exit(2)
    startModes(opts)

def startModes(opts):
    for opt, arg in opts:
        if opt in ('-d', "--display"):
            printModeEnteringInformation("Displaying-Mode")
            runDisplay()
        #TODO Implement!
        elif opt in ("-c", "--conversation"):
            printModeEnteringInformation("Conversation-Mode")
            runConversation()

def printModeEnteringInformation(modeName):
    print("Entering " + modeName)

def printTitle():
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
