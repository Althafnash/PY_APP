def guess():
    # A guess game 
    # The answer here is the number we should Guess (you can change it) you eill get three tries (you can change it also)
    answer = 7
    guess_count   = 0
    guess_limit   = 3
    print("------------------------------------------------------------")
    # When the Number of gusees is not equal to this while loop will run
    while   guess_count < guess_limit:
        # User input us taken 
        # you also have a clue
        print("CLUE :It is a number between 1-10")
        Guess = int(input("Your_Guses: "))
        # Add one to the count 
        guess_count += 1
        # if the guess is equal to the number then it will print you won
        if Guess == answer:
            print("You_Won")
            break
    else:
        # or else if you did not guess the number this will run
        print("You_Falied")
    print("------------------------------------------------------------")

