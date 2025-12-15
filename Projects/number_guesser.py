import random

try:
    upper_value = int(input("Type a number (0-50): "))
    if 0 <= upper_value <= 50:
        print("valid input.")
    else:
        print("Number must be between 0 to 50.")
        quit()
except ValueError:
    print("Invalid input. please enter a valid integer.")
    quit()

guesses = 0
random_num = random.randint(0, upper_value)

while True:
    guesses += 1
    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print('Please type a number next time.')
        continue

    if user_guess == random_num:
        print("You got it!")
        break
    else:
        if user_guess > random_num:
            print("You were above the number!")
        else:
            print("you were below th number!")

print("\t=========================")
print("\t You got it in",guesses, "guesses")
print("\t=========================")