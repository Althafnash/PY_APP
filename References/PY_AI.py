# This is my python ai i created with all the app funcatinallities and also speech recongination system 
# Feel free to use it 
# Befroe using you should have the following installed 
#       Python 
#       speech_recognition
#       pyttsx3
#       pywhatkit
#       wikipedia
#       tkinter
#       cv2
#       winsound
#       BeautifulSoup
#       psutil

import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import tkinter as tk
import tkinter.ttk as ttk
from time import strftime
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess 
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import cv2
import winsound
import time
import requests
from bs4 import BeautifulSoup
import psutil

listener = sr.Recognizer()
speak = pyttsx3.init()
# ==========================================================================================================================
# math funcations 

def Power():
    input = input("Enter the Number ::")
    input2 = input("Enter the power of number ::")
    return input * input2

def Math_engine():
        Input_command = input("Enter what you want to search :: ")
        if("power" in Input_command):
            Power()

# ==========================================================================================================================
# funcations 
def webcam():
    cam = cv2.VideoCapture(0) 
    while cam.isOpened(): 
        ret, frame1 = cam.read() 
        if cv2.waitKey(10) ==  ord('q'):
            break
        cv2.imshow('Camera',frame1) 
def camara():
    cam = cv2.VideoCapture(0) 
    while cam.isOpened(): 
        ret, frame1 = cam.read() 
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray , (5,5) , 0 )
        _ , tresh = cv2.threshold(blur ,29 ,255 , cv2.THRESH_BINARY)
        dialated = cv2.dilate(tresh ,None , iterations=3)
        contorus , _ = cv2.findContours(dialated , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE )
        #cv2.drawContours(frame1 , contorus , -1 , (0 , 0 , 225) , 2)
        for c in contorus:
            if cv2.contourArea(c)  < 5000:
                continue
            x,y,h,w = cv2.boundingRect(c)
            cv2.rectangle(frame1 , (x,y),(x+w ,y+h),(0 , 0 , 225) , 2)
            winsound.Beep(500,200)
        if cv2.waitKey(10) ==  ord('q'):
            break
        cv2.imshow('Camera',frame1) 

def Scrapper():
    url = input("Enter URL:: ")
    print("Just type an HTML tag you want to extract ")
    print("Eg::p")
    Tag = input("What do you want to extract :: ")

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content , 'lxml')
    headlines = soup.find_all(Tag)

def Bandwidth():
    last_recived = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total =last_recived + last_sent

    while True:
        bytes_recived = psutil.net_io_counters().bytes_recv
        bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_total = bytes_recived + bytes_sent

        new_recived = bytes_recived - last_recived
        new_sent = bytes_sent - last_sent
        new_total = bytes_total - last_total

        mb_new_recived = new_recived / 1024 / 1024
        mb_new_sent = new_sent / 1024 / 1024 
        mb_new_total = new_total / 1024 / 1024

        print(f"{mb_new_recived:.2f} MB received , {mb_new_sent:.2f} MB sent , {mb_new_total:.2f} MB total")

        last_recived = bytes_recived
        last_sent = bytes_sent
        last_total = bytes_total

        time.sleep(1)

print("------------------------Minecraft_App(ignore)--------------------------------------")
def Minecraft():
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

print("------------------------IGRNORE THIS THING --------------------------------------")

def calculator() :
    print("------------------------------------------------------------")
    print("\n" + "Calculator")
    FristNumber  = input( " Enter Frist number : ")
    SecondNumber  = input(" Enter Sceond number : ")
    print("\n" + "Answer")
    print(int(FristNumber) + int(SecondNumber))
    print("------------------------------------------------------------")


def guess():
    answer = 7
    guess_count   = 0
    guess_limit   = 3
    print("------------------------------------------------------------")
    while   guess_count < guess_limit:
        print("CLUE :It is a number between 1-10")
        Guess = int(input("Your_Guses: "))
        guess_count += 1
        if Guess == answer:
            print("You_Won")
            break
    else:
        print("You_Falied")
    print("------------------------------------------------------------")

def weight(): 
    weight = ""
    print("------------------------------------------------------------")
    weight = int(input("weight: "))
    unit = input("(L)bs or (k)g: ")
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"You are {converted} (k)g")
    else:
        converted = weight / 0.45
        print(f"You are {converted} (L)bs")
    print("------------------------------------------------------------")

def Clock():

    root = tk.Tk()
    root.title("clock")

    def time():
        string = strftime('%H:%M:%S %p')
        lable.config(text=string)
        lable.after(1000,time)

    lable = tk.Label(root ,font=("ds-digital", 80) , bg="black" ,fg="lightgreen" )
    lable.pack(anchor="center")
    time()

    root.mainloop()

def IDE():

    IDE = Tk()

    file_path = ""

    def set_file_path(path):
        global file_path
        file_path = path

    def open_file():
        path = askopenfilename(filetypes=[("Python Files", "*.py")])
        with open(path , 'r') as file:
            code = file.read()
            editor.delete("1.0" , END)
            editor.insert("1.0" , code)
            set_file_path(path)  

    def save_as():
        if file_path == '':
            path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
        else:
            path = file_path
        with open(path , "w") as file:
            code = editor.get("1.0" , END)
            file.write(code)
            set_file_path(path)

    def run():
        if file_path ==  '':
            save_prompt = Toplevel()
            text = Label(save_prompt , text="plesae save the file ")
            text.pack()
            return
        command = f'Python {file_path}'
        process = sub.Popen(command, stdout=subprocess.PIPE ,stderr=subprocess.PIPE , shell=True)
        output , error = process.communicate()
        code_output.insert('1.0', output)
        code_output.insert('1.0', error)

    menu_bar = Menu(IDE)

    run_bar = Menu(menu_bar , tearoff=0)
    run_bar.add_command(label="Run" , command=run)
    menu_bar.add_cascade(label="Run" , menu=run_bar)
    IDE.config(menu=menu_bar)

    file_bar = Menu(menu_bar , tearoff=0)
    file_bar.add_command(label="save" , command=save_as)
    file_bar.add_command(label="open" , command=open_file)
    file_bar.add_command(label="save as" , command=save_as)
    file_bar.add_command(label="Exit" , command=exit)
    menu_bar.add_cascade(label="File" , menu=file_bar)
    IDE.config(menu=menu_bar)

    IDE.title("NashIDE")
    editor = Text(bg="blue" , fg="red")
    editor.pack()

    code_output = Text(height=10 , bg="black" , fg="lightgreen")
    code_output.pack()

    IDE.mainloop()


def commands():
    
    root = tk.Tk()
    root.title("ALEXA Commands")
    code_output = Text(height=10 , bg="blue" , fg="lightgreen")
    root.geometry("200x1000")

    text1 = f"say play  and any song on youtube ... "
    text2 = f"It search for the thing you said  ... "
    text3 = f"Shows a digital clock  ... "

    label = tk.Label(root , text="commands"  )
    label.pack()

    label1 = tk.Label(root , text="play" , bg="green")
    label1.pack()
    label1 = tk.Label(root , text=text1   )
    label1.pack()

    label1 = tk.Label(root , text="search for" , bg="green")
    label1.pack()
    label1 = tk.Label(root , text=text2   )
    label1.pack()

    label1 = tk.Label(root , text="search for" , bg="green")
    label1.pack()
    label1 = tk.Label(root , text=text3   )
    label1.pack()

    root.mainloop()


def talk(text):
    speak.say(text)
    speak.runAndWait()

string = strftime('%H:%M %p')
talk("welcome back sir " + "the time is " + string )

def start_alexa():
    command = "" 
    try:
        with sr.Microphone() as source:
            print("listening .....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa" , "")
    except:
        pass
    return command


def run_alexa():
    replace = ""
    command = ""
    command = command
    person  = ""
    print("say alexa open ui to list commands ")
    command = start_alexa()
    if 'play' in command:
        replace = command.replace("play" , "")
        talk("playing" + replace)
        pywhatkit.playonyt(replace)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S %p ") 
        talk("The current time is " + time)
    elif "search for" in command:
        talk("searching on wikipedia sir")
        person = command.replace("search for" , "")
        person.lower()
        info = wikipedia.summary(person , 1)
        talk(info)
    elif "show clock" in command:
        talk("showing the clock sir")
        Clock()
    elif "open code editor" in command:
        talk("opening nash IDE sir")
        IDE()
    elif "open weight converter" in command:
        talk("opening weight convetor sir")
        weight()
    elif "Quit" in command:
        exit()
    elif "guess game" in command:
        talk("opening guess game sir")
        guess()
    elif "open calculator" in command:
        talk("opening calculator sir")
        calculator()
    elif "minecraft" in command:
        talk("opening minecraft softwear sir")
        Minecraft()
    elif "show network" in command:
        talk("sir your system network adapters ")
        sub.run("ipconfig / all" , shell=True)
    elif "show disks" in command:
        talk("opening sir")
        sub.run("diskpart" , shell=True)
    elif "show system info" in command:
        talk("showing system infomation sir")
        sub.run("SYSTEMINFO" , shell=True)
    elif "on webcam" in command:
        talk("opening webcam sir")
        webcam()
    elif "open softwear " in command:
        talk("opening movement dedecition softwear sir")
        camara()
    elif "open ui" in command:
        talk("ok sir ")
        commands()
    elif "openserver" in command:
        talk("ok sir ")
        subprocess.call("I:\\codeing\\website\\website.bat")
    elif "search website" in command:
        talk("ok sir ")
        Scrapper()
    elif "monitor bandwidth" in command:
        talk("ok sir ")
        Bandwidth()
    elif "Math engine" in command:
        talk("ok sir ")
        Math_engine()
    else:
        talk("sorry sir i did not understand that")


time.sleep(10)
while True:
    run_alexa() 