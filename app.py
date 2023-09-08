from time import strftime
from Nash_module_calculator import calculator
from Nash_modules_talk import talk
from Nash_modules_client import client
from Nash_modules_geoloc import geo 
from Nash_modules_guess import guess
from Nash_modules_minecraft import Minecraft
from Nash_modules_server import server
from Nash_modules_webcam import face
from Nash_modules_clock import Clock
from Nash_modules_weight import weight
from Nash_modules_IDE import IDE
from Nash_module_image_opener import opener 



string = strftime('%H:%M %p')
talk("welcome back sir " + "the time is " + string )
talk("How may i help you ")
talk("Below are my python projects")
print("""
        1   -   Face detector 
        2   -   Geo locator
        3/3.1   Sever/client
        4   -   Guess Game
        5   -   Minecraft
        6   -   Clock
        7   -   Weight convertor
        8   -   IDE
        9   -   Image opener
""")
command = input("What do you want to see ")
if command == "1":
        face()
elif command == "2":
        geo()
elif command == "3":
        server() 
elif command == "3.1":
        client()
elif command == "4":
        guess()
elif command == "5":
        Minecraft()
elif command == "6":
        Clock()
elif command == "7":
        weight()
elif command == "8":
        IDE()
elif command == "9":
        opener()