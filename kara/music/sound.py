#this is probably wrong

class sound:
    import ccircle
    import time
    import math

    def __init__(self):
        #idk



        mysound = ccircle.Sound()

        for x in range(44100):
            t = x / 44100
            mysound.addSample(sin(2 * pi * 440 * t))

        mysound.play()
        time.sleep(1)



