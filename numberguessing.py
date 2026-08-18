 
print("\n dum unte num guess karo")
secret_number = 7 
print("\nHINT:jersey number of a GOAT")

#until the user guess the correct num while loop runs
while True:

    #user can enter their guessing number
    guess = int(input("Guess a number between 1 and 50: "))

    #if user num is greater than secret num if block executes
    if guess > secret_number:
        print("Too high! Try again")

    #if less then elif executes
    elif guess < secret_number:
        
        print("Too low! Try again")

    #if user guess the secret num else block executes
    else:
        print(" suieeeeeeeeeeeeee")
        print("\nronaldo"*67)

        #to stop the loop
        break
