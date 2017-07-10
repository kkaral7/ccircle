#myList= ['string!!!', "double quote" , 1.337,3545435353]
#for thing in myList:
    #print(thing)

import ccircle
"""from math import*
window = ccircle.Window()
window.toggleMaximized()

points = []


while window.isOpen():
    window.clear(0.5,0.2,0.2)
    mx, my = window.getMousePos()


    if ccircle.isMouseDown('left'):
        points.append((mx,my))



    for point in points:
        window.drawRect(point[0],point[1],15,60,0.6,0.4,0.7)





    # ==   equal to
    #!= not equal to
    #>= greather than or equal to
    if len(points)>=7:
        window.drawRect(points[6][0],points[6][1], 60,60,1,0.1)

    window.drawCircle(mx, my, 8,0.1,1.0,1.0)
    window.update()

"""
window = ccircle.Window(1000,900)
window.toggleMaximized()

newimage = ccircle.Image(tictactoe.jpg)
while window.isOpen():

    window.clear(1,0.5,1.0)
    newimage.draw(200,200,300,200)

    window.update()


