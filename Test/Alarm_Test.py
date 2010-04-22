#!/usr/bin/python

import time
import subprocess
import sys
import msvcrt

alarm1 = int(raw_input("How many seconds (alarm1)? "))

while (1):
    time.sleep(alarm1)
    print "Alarm1"
    sys.stdout.flush()

    # Try to flush the buffer
    while msvcrt.kbhit():
        msvcrt.getch()

    print "Continue (Y/N)?[Y]"
    doit = msvcrt.getch()
    print "Input",doit
    if doit == 'N' or doit=='n':
        print "Exiting....."
        break
