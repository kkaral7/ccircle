class World:
    def __init__(self,name) :
        self.name = name
        self.objects = []

    def add(self,obj):
        self.objects.append(obj)

    def draw(self,window):
        window.drawRect(1000,1000,100,100)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)
