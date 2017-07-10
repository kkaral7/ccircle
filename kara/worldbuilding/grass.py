class Grass:
    def __init__(self,x,y,width,height):
        self.xx = x
        self.yy = y
        self.width = width
        self.height = height

    def draw(self,window):
        window.drawRect(self.xx,self.yy,self.height,self.width,0,1,0,)


    def update(self,dt):
        pass