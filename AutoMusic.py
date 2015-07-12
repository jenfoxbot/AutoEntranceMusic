#Trigger music using IR sensor
import os
import time

import RPi.GPIO as GPIO
from subprocess import Popen

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.IN)

file = '/home/pi/Desktop/projects/example.mp3'
file2 = file

try:
        print "IR Breakbeam Test (CTRL+C to exit)"
        time.sleep(2)
        print "Ready!"

        while True:        
                if (GPIO.input(25) == 0):
                        print ('Motion Detected.')
                        #os.system('omxplayer file')
                        omxp = Popen(['omxplayer', file])
                if GPIO.input(24) == 0:
                        print ('Motion Detected.')
                        omxp = Popen(['omxplayer', file2])
                time.sleep(1)

except KeyboardInterrupt:
        print "\n Quit"

GPIO.cleanup()

