class balloon:
    def __init__(self,x,y,size,vx,vy,mass):
        self.x = x
        self.y = y
        self.size = size
        self.stringLength = 85
        self.vx = vx
        self.vy = vy
        self.fx = 0
        self.fy = 0
        self.mass = mass




    def draw(self,window):
        window.drawCircle(self.x,self.y,self.size+1,0,0,0)
        window.drawCircle(self.x,self.y,self.size,1,0.5,1)
        window.drawLine(self.x,self.y+self.size,self.x,self.y+self.size+self.stringLength)


    def apply_force(self,fx,fy):
        self.fx += fx
        self.fy += fy

    def update(self,dt):
        self.x += dt * self.vx  #chooses the direction of the balloons
        self.y -= dt * self.vy

        accel_x = self.fx/self.mass   #this is the force self.fx/self.mass
        accel_y =  self.fy/self.mass   #self.fy/self.mass
        self.vx +=  dt*accel_x
        self.vy +=  dt*accel_y
        self.fx = 0   # moving side speed
        self.fy = 0  #  moving up speed 

        if self.x > 800: self.x = 0   #keeps the balloons coming
        if self.x <0: self.x = 800
        if self.y > 700: self.y = 0
        if self.y < 0: self.y = 700





