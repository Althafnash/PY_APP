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