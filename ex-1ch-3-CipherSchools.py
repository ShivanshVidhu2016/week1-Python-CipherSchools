winning_number=2
guessed_number=int(input("enter a number to check: "))
if winning_number==guessed_number:
    print("You win")
else:
    if guessed_number<winning_number:
        print("too low")
    else:
        print("too high")    

