import ccircle
import musicworld
import time
import balloon
import random


window = ccircle.Window("Play My Garbage Game", 800,600)
my_world = musicworld.World('ballonworld')


for i in range(20):  #balloons
    x = random.randint(35,35)
    y = random.randint(900,900)
    size = random.randint(50,50)
    vx = random.randint(0,3)
    vy = random.randint(2,10)
    my_world.add(balloon.balloon(x,y,size,vx,vy))


# problem:   i need to set a key binding so the thing recgonizes where i click as the mouse position




start = time.time()
dt = 1.0/60.0


while window.isOpen():
    window.clear(0,0.3,0.7)
    my_world.update(40* dt)
    my_world.draw(window)
    if ccircle.isMouseDown('left'):
        mx, my = window.getMousePos()


        for bn in list(my_world.objects):
            a = (bn.x - mx)
            b = (bn.y - my)
            pyg = a ** 2 + b ** 2
            c = size
# fix this
            if (c ** 2) > pyg: #clicked a balloon
                print(" balloon")
                my_world.objects.remove(bn)
                # make balloon dissapear + add function that makes a note
            if (c ** 2) <= pyg:  # didn't click a balloon
                print("not a balloon")

    window.update()


    now = time.time()
    dt = now - start
    start = now