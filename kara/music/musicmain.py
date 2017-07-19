import ccircle
import musicworld
import time
import balloon
import random
import badballoons
import background
import sound


window = ccircle.Window("If you wait like 20 seconds, the game is better, rated E for everyone", 800,600)
my_world = musicworld.World('balloonworld')


for n in range(3000):   #background
    x = random.randint(0,900)
    y = random.randint(0,600)
    width = random.randint(4,5)
    height = random.randint(4,5)
    size = 1    # this doesn't do anything
    vx = 0
    vy = 0
    my_world.add(background.background(x,y,width,height,size,vx,vy))

def addballoon():
    x = random.randint(30, 35)
    y = random.randint(800, 900)
    size = random.randint(40, 40)
    vx = random.randint(0, 3)
    vy = random.randint(2, 10)
    mass = random.randint(4,20)
    my_balloon = balloon.balloon(x, y, size, vx, vy,mass,True)
    my_world.add(my_balloon)


for i in range(20):  #balloons
    addballoon()

def addbadballoon():
    x = random.randint(35,35)
    y = random.randint(900,900)
    size = random.randint(40,40)
    vx = random.randint(0,3)
    vy = random.randint(1,10)
    mass = random.randint(5,10)
    bad_balloon = badballoons.badballoons(x,y,size,vx,vy,mass,False)
    my_world.add(bad_balloon)


for th in range(20): #badballoons
    addbadballoon()


start = time.perf_counter()
dt = 1.0/60.0



while window.isOpen():
    window.clear(0,0.5,0.7)
    my_world.update(dt)
    my_world.draw(window)
    for xn in list(my_world.objects):
        if len(my_world.objects)<=40: #and xn.good == True:    # adds more balloons when they get deleted
            for nn in range(6):
                addballoon()
                addbadballoon()
        #elif len(my_world.objects)<= 10 and xn.good == False:
            #for yn in range(5):



    for ev in my_world.objects:
        ev.apply_force(5,8)


    if ccircle.isMouseDown('left'):
        mx, my = window.getMousePos()



        for ln in list(my_world.objects):   #this part removes objects that go past certain boundaries
            if ln.x < - ln.size and ln.x > 1000+ln.size:
                my_world.objects.remove(ln)
            if ln.y < 0-ln.size:
                my_world.objects.remove(ln)
        for bn in list(my_world.objects):
            a = (bn.x - mx)
            b = (bn.y - my)
            pyg = a ** 2 + b ** 2
            c = bn.size

            if (c ** 2) > pyg: #clicked a balloon    #note addition should be here
                my_world.objects.remove(bn)
                #if bn.good == True:
                    #freq = 150
                    #ssound = sound.sound(freq)
                    #my_world.addnote(ssound)
                    #pass

                #else:
                    #pass
            if (c ** 2) <= pyg:  # didn't click a balloon
                pass

    window.update()


    now = time.perf_counter()
    dt = now - start
    start = now