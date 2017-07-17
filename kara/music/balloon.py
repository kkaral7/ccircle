class balloon:
    def __init__(self,x,y,size,vx,vy):
        self.x = x
        self.y = y
        self.size = size
        self.stringLength = 70
        self.vx = vx
        self.vy = vy


    def draw(self,window):
        window.drawCircle(self.x,self.y,self.size,1,0.5,1)
        window.drawLine(self.x,self.y+self.size,self.x,self.y+self.size+self.stringLength)
        #100, 200, 100, 300

    def update(self,dt):
        self.x += dt * self.vx  #chooses the direction of the balloons
        self.y -= dt * self.vy

        if self.x > 800: self.x = 0   #keeps the balloons coming
        if self.x <0: self.x = 800
        if self.y > 800: self.y = 0
        if self.y < 0: self.y = 800
'''
        mx,my = window.getMousePos()
        #point1 = (self.x,self.y)  #idk is this how to assign a point?
        a = (x-mx)
        b = (y-my)
        c = size
        pyg = a**2 + b**2

        if (c**2) <= pyg:
            print ("hello")
            #make balloon dissapear + add function that makes a note
        if (c**2) > pyg:
            print ("bye")

'''


