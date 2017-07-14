#new main
import ccircle
import newworld
import random
import newcloud
import newcloud2
import newcloud3
import time
import newstar

window = ccircle.Window("world",800,600)
new_world = newworld.newworld("Aladdin")



for i in range(140):      #largest clouds
    x = random.randint(0,800)
    y = random.randint(400,700)
    size = random.randint(50,100)
    vx =  random.uniform(0,10)
    new_world.add(newcloud.newcloud(x,y,size,vx))

for n in range(100):     #2nd clouds
    x = random.randint(0,800)
    y = random.randint(450,700)
    size = random.randint(50,80)
    vx =  random.uniform(0,10)
    new_world.add(newcloud2.newcloud2(x,y,size,vx))

for t in range(120):  #3rd clouds
    x = random.randint(0,800)
    y = random.randint(500,800)
    size = random.randint(50,70)
    vx =  random.uniform(0,10)
    new_world.add(newcloud3.newcloud3(x,y,size,vx))

for nn in range(1): #stars
    x1 = random.randint(100,100)
    y1 = random.randint(80,80)
    x2 = random.randint(70,70)
    y2 = random.randint(150,150)
    x3 = random.randint(130,130)
    y3 = random.randint(150,150)
    vx = random.uniform(0,10)
    new_world.add(newstar.newstar(x1,y1,x2,y2,x3,y3,vx))
'''
for tt in range(1): #stars2
    x1 = random.randint(100,100)
    y1 = random.randint(280,280)
    x2 = random.randint(50,50)
    y2 = random.randint(130,130)
    x3 = random.randint(150,150)
    y3 = random.randint(130,130)
    vx = random.uniform(0,10)
    new_world.add(newstar.newstar(x1,y1,x2,y2,x3,y3,vx))
'''

# window.drawTri(100,100,50,200,150,200,1,1,1)
 # window.drawTri(100,230,50,130,150,130,1,1,1)




start = time.time()
dt = 1.0/60.0

while window.isOpen():
    window.clear(0.1,0.1,0.1)
    new_world.update(5*dt)
    new_world.draw(window)

    window.update()

    now = time.time()
    dt = now - start
    start = now