class newworld:
    def __init__(self,name):
        self.name = name
        self.objects = []

    def add(self,obj):
        self.objects.append(obj)

    def draw(self, window):
        window.drawRect(800,400,900,800,1,1,1)
        for obj in self.objects:
            obj.draw(window)

    def update(self,dt):
        for obj in self.objects:
            obj.update(dt)
