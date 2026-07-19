import random 

computer=random.randint(0,100)

#computer_guess
#random_number



score=0
attemps=0
while True:
    
    
    
    try:
        person=int(input("Guess a number between0to100:  "))
        #input_number_from_person
        if person > 100 or person < 0:
            print("please enter a number between 0 to 100")
            continue
    except ValueError:
        print("just intieger number")
        continue
    attemps+=1
    

    if computer > person:
        print(f"Oh ")
        print("Your number smaller than computer number")
        
    elif person > computer :
        print(f"Oh")
        print("Your number larger than computer number")
        
    else:
        print("\nYOu won the game")
        print(f"The computer number was {computer}")
        score+=1
        print(f"Your Score is {score}")
        print(f"You guessed it in {attemps} attemp")
        again=input("DO YOU WANT TO PLAY AGAIN?")
        if again.capitalize() =="Yes":
            continue
        elif again.capitalize() == "No":
            break
        
        
        
