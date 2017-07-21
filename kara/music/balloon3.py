class balloon3:

    def __init__(self,x,y,size,vx,vy,mass,good):
            self.x = x
            self.y = y
            self.size = size
            self.stringLength = 85
            self.vx = vx
            self.vy = vy
            self.fx = 0
            self.fy = 0
            self.mass = mass
            self.good = good



    def draw(self, window):
        window.drawCircle(self.x, self.y, self.size + 1, 0, 0, 0)
        window.drawCircle(self.x, self.y, self.size,0.6,0.3,0.7)
        window.drawLine(self.x - 14, self.y - 8, self.x - 14, self.y + 15, 5, 1, 0, 0)  # eyes
        window.drawLine(self.x + 14, self.y - 8, self.x + 14, self.y + 15, 5, 1, 0, 0)
        window.drawLine(self.x - 25, self.y - 14, self.x - 5, self.y - 2, 3, 0, 0, 0)  # angry eyebrows!
        window.drawLine(self.x + 2, self.y - 3, self.x + 22, self.y - 14, 3, 0, 0, 0)
        window.drawLine(self.x, self.y + self.size, self.x, self.y + self.size + self.stringLength)


    def apply_force(self,fx,fy):
        self.fx += fx
        self.fy += fy

    def update(self, dt):
        self.x += dt * self.vx  # chooses the direction of the balloons
        self.y -= dt * self.vy

        accel_x = self.fx / self.mass  # this is the force self.fx/self.mass
        accel_y = self.fy / self.mass  # self.fy/self.mass
        self.vx += dt * accel_x
        self.vy += dt * accel_y
        self.fx = 0  # moving side speed
        self.fy = 0  # moving up speed



        if self.x > 800: self.x = 0 #keeps the baloons coming
        if self.x < 0: self.x = 800
        if self.y > 600: self.y = 0
        if self.y < 0: self.y = 600
