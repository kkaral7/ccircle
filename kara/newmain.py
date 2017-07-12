#new main
import ccircle
import newworld
import random
import newcloud
import newcloud2
import newcloud3
import time

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

for t in range(50):  #3rd clouds
    x = random.randint(0,800)
    y = random.randint(450,700)
    size = random.randint(50,80)
    vx =  random.uniform(0,10)
    new_world.add(newcloud3.newcloud3(x,y,size,vx))


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