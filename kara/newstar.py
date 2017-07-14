class newstar:
    def __init__(self,x1,y1,x2,y2,x3,y3,vx):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.vx = vx

    def draw(self,window):
        window.drawTri(self.x1,self.y1,self.x2,self.y2, self.x3,self.y3,self.vx,0.4,0.5,0.2,)


    def update(self,dt):
        pass


