print("------------------------Minecraft_App(ignore)--------------------------------------")
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
def Minecraft():
     # bulid useing the code in github/ursina
     # press w,a,s,d to mave
     # left click to create a cube
     # right click to destroy a cube


    print("--------------------------------------------------------------")
    print("YOU CAN PRTICE MINECRAF HERE")
    print("bulid useing the code in github/ursina")
    print("left click to create a cube")
    print("left click to create a cube")
    print("right click to destroy a cube")
    print("CRAETED BY MOHAMMED ALTHAF")
    print("IF YOU WANT TO EXIT PRESS CTR+SHIFT+Q")
    print("----------------------------------------------------------------")
    app = Ursina()

    class Voxel(Button):
        def __init__(self, position=(0,0,0)):
            super().__init__(
                parent = scene,
                position = position,
                model = 'cube',
                origin_y = .6,
                texture = 'white_cube',
                color = color.white,
                highlight_color = color.blue,
            )


        def input(self, key):
            if self.hovered:
                if key == 'left mouse down':
                    voxel = Voxel(position=self.position + mouse.normal)

                if key == 'right mouse down':
                    destroy(self)


    for z in range(20):
        for x in range(20):
            voxel = Voxel(position=(x,0,z))


    player = FirstPersonController()
    app.run()

print("------------------------IGRNORE THIS THING S***T--------------------------------------")

