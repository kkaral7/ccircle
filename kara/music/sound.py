import ccircle
import time
#import util
from math import *

class sound:

    def __init__(self):
        pass

#ill wait on this for now

window = ccircle.Window('This is hard')
mysound = ccircle.Sound()

def sawtooth(t, f):
    return 2.0 * ((t * f) % 1.0) - 1.0

def sine(t, f):
    return sin(2.0 * pi * t * f)

for i in range(44100):
    t = i / 44100
    mysound.addSample(sine(t,150 ))



mysound.play()
time.sleep(1)


