#tictactoe
import ccircle

window = ccircle.Window("Let's play tic tac toe",1000,900)
window.toggleMaximized()
points = []

'''class Board(object):
    def _init_(self,settings):
        self.settings = settings
    
'''


while window.isOpen():
                #red,green,blue

    window.clear(1,0.5,1.0)
    mx, my = window.getMousePos()
    window.drawLine(300,300,1000,300,5,0,0,0)#horizontal
    window.drawLine(300,600,1000,600,5,0,0,0)
    window.drawLine(500,100,500,800,5,0,0,0)#vertical
    window.drawLine(800,100,800,800,5,0,0,0)
    if ccircle.isMouseDown('left'):
        points.append((mx,my))



    for point in points:
        window.drawCircle(point[0], point[1], 10, 3,  0.2, 0.8, 0.7)


    if len(points)>=7:
        window.drawCircle(points[6][0],points[6][1],10,60, 0.2, 0.8, 0.7)

    window.drawCircle(mx, my, 10,8,0.2,0.8,0.7)
    window.update()

