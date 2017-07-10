#coding is hard who did this
import ccircle

window = ccircle.Window("Let's play tic tac toe",1000,900)
window.toggleMaximized()
points = []

'''class Board(object):
    def _init_(self,settings):
        self.settings = settings

    def get_mouse(self):
        mx, my - window.getMousePos()
        points = []

        if ccircle.isMouseDowm('left'):
            points.append((mx,my))

            for point in points:
                window.drawCircle(point[0],point[1], 15,60,0,0,0)

'''


while window.isOpen():
                #red,green,blue

    window.clear(1,0.5,1.0)
    mx, my = window.getMousePos()
    window.drawLine(0,300,2000,300,5,0,0,0)
    window.drawLine(0,666,2000,666,5,0,0,0)
    window.drawLine(500,0,500,1000,5,0,0,0)
    window.drawLine(1000,0,1000,1000,5,0,0,0)
    if ccircle.isMouseDown('left'):
        points.append((mx,my))

    for point in points:
        window.drawRect(point[0],point[1],15,60,0.6,0.4,0.7)