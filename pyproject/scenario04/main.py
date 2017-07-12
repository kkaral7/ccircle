import ccircle
import connection
con = connection.create()
con.send('set_name', {'name': 'swiggity'})
args = {
    "vx": 0,
    "vy": 0,

}

# Write code to make money and kill the evil cat!
# See readme.txt

"""
while(True):
    

    left = ccircle.isMouseDown('left')
    right = ccircle.isMouseDown('right')
    up = ccircle.isMouseDown('up')
    down = ccircle.isMouseDown('down')
    if left:
        vx -= 40
    if right:
        vx += 40
    if up:
        vy -= 40
    if down:
        vy += 40

    con.send('set_velocity', {"vx": vx,"vy": vy})


#while(True):
    (con.send('get_player_ids'))
(con.send('get_money'))
send_money (id, amount)   
'''









































