import ccircle
import time
import random
import util
from math import *

window = ccircle.Window('Lab: Audio Synthesis')
mysound = ccircle.Sound()
newsound = ccircle.Sound()
a = ccircle.Sound()

def sawtooth(t, f):
    return 2.0 * ((t * f) % 1.0) - 1.0

def sine(t, f):
    return sin(2.0 * pi * t * f)

for i in range(44100):
    t = i / 44100
    mysound.addSample(sine(t,659 )) #E
    newsound.addSample(sine(t,587)) #   #D
    a.addSample(sine(t,523 ))  # C
    newsound.addSample(sine(t,587))  # #D
    mysound.addSample(sine(t,659))  # E
    mysound.addSample(sine(t, 659))  # E
    mysound.addSample(sine(t, 659))  # E
    newsound.addSample(sine(t, 587))  # #D
    newsound.addSample(sine(t, 587))  # #D
    newsound.addSample(sine(t, 587))  # #D


mysound.play()
time.sleep(1)
newsound.play()
time.sleep(1)
a.play()
time.sleep(1)
newsound.play()
time.sleep(1)
mysound.play()
time.sleep(1)
mysound.play()
time.sleep(1)
mysound.play()
time.sleep(1)
newsound.play()
time.sleep(1)
newsound.play()
time.sleep(1)
newsound.play()
time.sleep(1)

