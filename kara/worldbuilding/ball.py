class Ball:
    def __init__(self,x,y):
        self.x= x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.fx = 0
        self.fy = 0
        self.mass = 1
        self.rgb = (1, 0, 0.2)

    def apply_force(self,fx,fy):
        self.fx = fx
        self.fy = fy

    def draw(self,window):
        window.drawCircle(self.x,self.y,16, self.rgb[0], self.rgb[1], self.rgb[2])

    def update(self,dt):
        accel_x = self.fx / self.mass
        accel_y = self.fy / self.mass
        self.vx += dt * accel_x
        self.vy += dt * accel_y
        self.x += dt * self.vx
        self.y += dt * self.vy
        self.fx = 0
        self.fy = 0

        if self.y > 500:
            self.vy *= -1.0
            self.y = 500
            # if we're red, turn blue. If blue turn green. If green turn red.
           # if self.rgb[0] == 1:
            #    self.rgb = (0.1, 0.1, 1)
            #if self.rgb[2] == 1:
             #   self.rgb = (0.1, 1, 0.1)
            #if self.rgb[1] == 1:
             #   self.rgb = (1, 0.1, 0.1)"""
        if self.y <50:
            self.vy *= 1.0

