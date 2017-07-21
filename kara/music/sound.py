import ccircle
import time
#import util
from math import *


def sawtooth(t, f):
    return 2.0 * ((t * f) % 1.0) - 1.0

def sine(t, f):
    return sin(2.0 * pi * t * f)


def creategoodnote(freq):
    mysound = ccircle.Sound()
    for i in range(22050):
        t = i / 44100
        mysound.addSample(sine(t,freq))

    mysound.play()





