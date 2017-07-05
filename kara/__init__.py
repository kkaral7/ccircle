import ccircle
from math import*

window = ccircle.Window("Let's just get it working!",900,800)
while window.isOpen():
                #red,green,blue
    window.clear(0,0.5,0.9)
    window.drawRect(0,400,900,800,0,0.5,0)
    window.drawCircle(100,100,80,0.8,0.6,0)#smaller y goes higher
    window.drawCircle(500,600,50 )
    window.drawRect(490,560,30,30,0,0,0)
    window.drawRect(520,590,28,30,0,0,0)
    window.drawRect(460,590,30,30,0,0,0)
    window.drawRect(490,618,30,30,0,0,0)


    window.update()