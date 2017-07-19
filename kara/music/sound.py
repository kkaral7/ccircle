import ccircle
import time
#import util
from math import *


class sound:
    def __init__(self,freq,window,mysound):
        self.freq = freq
        self.window = ccircle.Window('Lab: Audio Synthesis')
        self.sound = mysound

    def sawtooth(t, f):
        return 2.0 * ((t * f) % 1.0) - 1.0

    def sine(t, f):
        return sin(2.0 * pi * t * f)

    def addnote(self):
        for i in range(44100):
            t = i / 44100
            mysound = ccircle.Sound()
            mysound.addSample(sine(t,self.freq))

        mysound.play()
        time.sleep(1)



