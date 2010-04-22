
#!/usr/bin/python

import time
import sys


def runAlarm( time_list ):
    minute = 5     # one minute = 5 seconds

    while (1):
        for t in time_list:
            cur_time = t 
            print cur_time
            while ( cur_time > 0 ):
                time.sleep(minute)
                cur_time -= 1
                print cur_time
               
            print "Alarm:",t
            sys.stdout.flush();
            doit = raw_input("Continue (Y/N)?[Y]: ")
            if doit == 'N' or doit=='n':
                print "Exiting....."
                return


if __name__ == "__main__":
    sys.stdout.flush();
    alarm1 = int(raw_input("How many minutes (alarm1)? "))
    sys.stdout.flush();
    alarm2 = int(raw_input("How many minutes (alarm2)? "))
    runAlarm( [ alarm1, alarm2 ] )
