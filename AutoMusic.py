import time
from threading import Thread

import RPi.GPIO as GPIO
import subprocess


class AutoTrigger():
    def call_omxpalyer(self):
        print ("playing " + self.file_path)
        pid = subprocess.call(['omxplayer', self.file_path], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        self.is_running = False

    def play_song(self):
        if not self.is_running:
            self.song_thread = Thread(target=self.call_omxpalyer, args=())
            self.song_thread.start()
            self.is_running = True

    def __init__(self, pin, file_path):
        self.pin = pin
        self.file_path = file_path
        self.is_running = False
        GPIO.setup(pin, GPIO.IN)
        '''
            This is a hack (the callback) thanks for python closures!
        '''
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=lambda x: self.play_song(), bouncetime=10)

    
def main():
    GPIO.setmode(GPIO.BCM)
    AutoTrigger(25, '/home/pi/Desktop/projects/ETHEREAL.wav')
    AutoTrigger(24, '/home/pi/Desktop/projects/PULSE2.wav')

    print ("Ready: !")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()        


if __name__ == '__main__':
    main()
