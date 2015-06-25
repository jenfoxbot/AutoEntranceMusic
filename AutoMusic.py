#Trigger music using IR sensor
import os
import time
from subprocess import Popen

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

file = '/home/pi/Desktop/example.mp3'

try:
        print "IR Breakbeam Test (CTRL+C to exit)"
        time.sleep(2)
        print "Ready!"

        while True:        
                if GPIO.input(23) == 0:
                        print ('Motoin Detected.')
                        #The following command prints a description of music file  
                        omxp=  Popen(['omxplayer', file])
                time.sleep(1)

except KeyboardInterrupt:
        print "\n Quit"

GPIO.cleanup()
