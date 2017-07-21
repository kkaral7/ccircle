class background:
    def __init__(self,x,y,width,height,size,vx,vy,good):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = size
        self.vx = vx
        self.vy = vy
        self.fx = 0
        self.fy = 0
        self.mass = 0
        self.good = good

    def draw(self,window):  # make triangles maybe
        window.drawRect(self.x,self.y,self.height,self.width,0.3,0.3,1,)

    def apply_force(self,fx,fy):  # produces 0 force
        self.fx += fx- fx
        self.fy += fy - fy


    def update(self,dt):
        pass