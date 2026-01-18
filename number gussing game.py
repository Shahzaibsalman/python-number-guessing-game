import random

print("Welcome to Number Guessing Game")

# Computer number
com_number = random.randint(1, 100)

# Choose level
level = input("Enter game level (easy or hard): ").lower()

if level == "easy":
    chances = 10
elif level == "hard":
    chances = 5
else:
    print("Invalid level")
    exit()

# Function
def find_number(user_number):
    if user_number == com_number:
        print("🎉 You win!")
        return True
    elif user_number < com_number:
        print("Your number is smaller than computer")
    else:
        print("Your number is greater than computer")
    return False

# Game loop
while chances > 0:
    print(f"Chances left: {chances}")
    user_number = int(input("Enter a number (1 to 100): "))

    if find_number(user_number):
        break

    chances -= 1

if chances == 0:
    print("😢 You lose!")
    print("Correct number was:", com_number)



