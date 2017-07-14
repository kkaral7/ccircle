import ccircle
import time
import util
from math import*

window  = ccircle.Window('Lab: Audio Synthesis')
mysound = ccircle.Sound()

for x in range(44100):
    t = x/44100
    mysound.addSample(sin(2*pi*440*t))

mysound.play()
time.sleep(1)