from time import strftime
from Nash_modules_calculator.py import calculator


calculator()
string = strftime('%H:%M %p')
talk("welcome back sir " + "the time is " + string )
talk("How may i help you ")
talk("Bleow are my python projects")
print("""
        1   -   Face detector 
        2   -   Geo locator
        3   -   Sever
        4 
""")
commnad = input("What do you want to see ")
if command == "1":
        face()
elif command == "2":
        geo()
elif command == "3":
        server()
        client()