#lets make even more clouds boiz

class newcloud3:
    def __init__(self,x,y,size,vx):
        self.x = x
        self.y = y
        self.size = size
        self.vx = vx


    def draw(self,window):
        window.drawCircle(self.x,self.y,self.size,1,0.3,1,0.6)

    def update(self,dt):
        self.x += dt * self.vx

        if self.x > 800: self.x = 0
        if self.x < 0: self.x = 800