import random

#function to check if guess is correct, greater or lesser than the correct one
def checknumber(req_answer, my_num, x):
    if my_num > req_answer:
        print("Your number is greater. Enter a less number")
    elif my_num < req_answer:
        print("Your number is less. Enter a greater number")
    else:
        print(f"You entered a correct number in {x} attempts.")
        return True

count=0

#ask the user for mini and max value and check if it is valid or not
while True:
    try: 
        mini= int(input("Enter the minimum number: "))
        maxi= int(input("Enter the maximum number: "))

        if mini >= maxi:
            print("Minimum number should be less than the maximum number. Please try again.")
        else:
            break  
    except Exception:
        print("Invalid input. Please enter valid integers.")

#get the random number
answer= random.randint(mini, maxi)

#ask for the guess and call the function to check if it is correct or not.
while True:
    try:
        count += 1
        guess= int (input("Enter your Guess: "))
        if checknumber(answer, guess, count ):
          break
    except Exception:
            print("Invalid input. Please enter valid integers.")