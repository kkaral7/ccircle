import ccircle
import musicworld
import time
import balloon
import random
import badballoons
import background
import sound
import balloon3

window = ccircle.Window("Click the pink balloons...or else... rated E for everyone", 800,600)
my_world = musicworld.World('balloonworld')
ww = 150
tt = 700
font = ccircle.Font('AldotheApache.ttf')
points = 0

for n in range(3000):   #background
    x = random.randint(0,2000)
    y = random.randint(0,900)
    width = random.randint(4,5)
    height = random.randint(4,5)
    size = 1    # this doesn't do anything
    vx = 0
    vy = 0
    my_world.add(background.background(x,y,width,height,size,vx,vy,False))

balloonlist = []
def addballoon():
    x = random.randint(15, 650)
    y = random.randint(800, 900)
    size = random.randint(40, 40)
    vx = random.randint(28, 47)
    vy = random.randint(20, 40)
    mass = random.randint(11,40)
    my_balloon = balloon.balloon(x, y, size, vx, vy,mass,True)
    my_world.add(my_balloon)
    balloonlist.append(my_balloon)

for i in range(12):  #balloons
    addballoon()

def addbadballoon():
    x = random.randint(0,600)
    y = random.randint(800,900)
    size = random.randint(40,40)
    vx = random.randint(17,33)
    vy = random.randint(20,40)
    mass = random.randint(13,19)
    bad_balloon = badballoons.badballoons(x,y,size,vx,vy,mass,False)
    my_world.add(bad_balloon)


for th in range(10): #badballoons
    addbadballoon()
def addballoon3():
    x = random.randint(0, 700)
    y = random.randint(800, 900)
    size = random.randint(40, 40)
    vx = random.randint(25, 48)
    vy = random.randint(20, 45)
    mass = random.randint(16,32)
    my_balloon3 = balloon3.balloon3(x, y, size, vx, vy,mass,False)
    my_world.add(my_balloon3)


for gg in range(8):  #balloon3
    addballoon3()


start = time.perf_counter()
dt = 1.0/60.0



while window.isOpen():
    window.clear(0,0.5,0.7)
    my_world.update(dt)
    my_world.draw(window,font,points)
    for xn in list(my_world.objects):
        if len(balloonlist) < 8:
            for trn in range(6):
                addballoon()
        if len(my_world.objects)<=3050:   # adds more balloons when they get deleted
            for nn in range(1):
                addballoon()
                addbadballoon()
                addballoon3()





    for ev in my_world.objects:
        ev.apply_force(5,10)


    if ccircle.isMouseDown('left'):
        mx, my = window.getMousePos()



        for ln in list(my_world.objects):   #this part removes objects that go past certain boundaries
            if ln.x < - ln.size and ln.x > 1300+ ln.size:
                my_world.objects.remove(ln)
            if ln.y < -200:  # 0 - ln.size
                my_world.objects.remove(ln)
        for bn in list(my_world.objects):
            a = (bn.x - mx)
            b = (bn.y - my)
            pyg = a ** 2 + b ** 2
            c = bn.size

            if (c ** 2) > pyg: #clicked a balloon    #note addition should be here
                my_world.objects.remove(bn)
                if bn.good == True or bn.good == True and bn.good == False:
                    ww *= 2**(1/12)
                    sound.creategoodnote(ww)
                    if ww > 566:
                        ww = 150
                    points = points + 5

                elif bn.good == False or bn.good == False and bn.good == True:
                    tt *= 2 **(1/12)
                    sound.creategoodnote(tt) #actually a bad note
                    window.clear(1, 0, 0)
                    if tt > 1700:
                         tt = 700
                    points = points - 5

            if (c ** 2) <= pyg:  # didn't click a balloon
                pass
    window.update()


    now = time.perf_counter()
    dt = now - start
    start = now