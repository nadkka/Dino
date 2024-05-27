#pip install ursina

from ursina import *
import random

app=Ursina()

window.color=color.white

dino= Animation( 
    'dino',
    collider='box',
    x=-5
)

label= Text(
    text=f'POINTS: 0',
    color=color.black,
    position=(-0.5,0.4),
    scale=(2,2,1)

    )

ground1= Entity(
    model='quad',
    texture='ground',
    scale=(50,0.5,1),
    z=1,
    y=-0.56
) 
ground2=duplicate(ground1, x=50)

grounds=[ground1, ground2]

cactus= Entity(
    model='quad',
    texture='cacti',
    collider='box',
    x=20,
    y=-0.05,
    scale=(0.6, 1, 1)
)


cacti=[]

def newCacti():
    new=duplicate(cactus,
    x=10+ random.randint(0,5))
    cacti.append(new)
    invoke(newCacti, delay=2)

newCacti()

points = 0

dzwiek= Audio(
    'sneakys.mp3',
    autoplay=True,
    look=True
)

sound= Audio(
    'assets_beep',
    autoplay=False
)

death= Audio(
    'dundundun.mp3',
    autoplay=False
)
number=6
def update():
    global points
    global number
    points+=0.1
    label.text= f'POINTS: {round(points)}'
    for ground in grounds:
        ground.x -=number *time.dt
        if points/100==0:
            ground.x-= number*2* time.dt 
        if ground.x< -35:
            ground.x+=100

    for c in cacti:
        c.x -= 6 * time.dt

    if dino.intersects().hit:
        dino.texture="hit"
        dzwiek.pause()
        application.pause()
        death.play()
        


def input(key):
    if key == 'space':
        if dino.y<0.01:
            sound.play()
            dino.animate_y(
                2,
                duration=0.4,
                curve=curve.out_sine
            )
            dino.animate_y(
                0,
                duration=0.4,
                delay=0.4,
                curve= curve.in_sine

            )




camera.orthographic=True
camera.fov= 10

app.run()