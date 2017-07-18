import ccircle
import musicworld
import time
import balloon
import random
import badballoons



window = ccircle.Window("Play my Garbage Game, rated E for everyone", 800,600)
my_world = musicworld.World('ballonworld')



def addballoon():
    x = random.randint(30, 35)
    y = random.randint(800, 900)
    size = random.randint(40, 40)
    vx = random.randint(0, 3)
    vy = random.randint(2, 10)
    mass = random.randint(4,20)
    my_balloon = balloon.balloon(x, y, size, vx, vy,mass)
    my_world.add(my_balloon)


for i in range(10):  #balloons
    addballoon()

def addbadballoon():
    x = random.randint(35,35)
    y = random.randint(900,900)
    size = random.randint(40,40)
    vx = random.randint(0,3)
    vy = random.randint(1,10)
    mass = random.randint(5,10)
    bad_balloon = badballoons.badballoons(x,y,size,vx,vy,mass)
    my_world.add(bad_balloon)


for th in range(20): #badballoons
    addbadballoon()


start = time.perf_counter()
dt = 1.0/60.0


while window.isOpen():
    window.clear(0,0.5,0.7)
    my_world.update(dt)
    my_world.draw(window)

    if len(my_world.objects)<=10:    # adds more balloons when they get deleted
        for nn in range(1):
            addballoon()


    for ev in my_world.objects:
        ev.apply_force(5,6)


    if ccircle.isMouseDown('left'):
        mx, my = window.getMousePos()

        for ln in list(my_world.objects):   #this part removes objects that go past certain boundaries
            if ln.x < - ln.size and ln.x > 1000+ln.size:
                my_world.objects.remove(ln)
            if ln.y < 0:
                my_world.objects.remove(ln)
        for bn in list(my_world.objects):
            a = (bn.x - mx)
            b = (bn.y - my)
            pyg = a ** 2 + b ** 2
            c = bn.size

            if (c ** 2) > pyg: #clicked a balloon
                my_world.objects.remove(bn)
                # add function that makes a note
            if (c ** 2) <= pyg:  # didn't click a balloon
                pass

    window.update()


    now = time.perf_counter()
    dt = now - start
    start = now