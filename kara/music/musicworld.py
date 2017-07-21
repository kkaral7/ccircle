import ccircle
class World:
    def __init__(self,name):
        self.name = name
        self.objects = []

    def add(self,obj):
        self.objects.append(obj)

    def draw(self,window,font,points):
        window.drawRect(1000,1000,100,100)
        scoreString = 'Score: ' + str(points)
        font.draw(scoreString,300,300,30,0,1,0)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)



