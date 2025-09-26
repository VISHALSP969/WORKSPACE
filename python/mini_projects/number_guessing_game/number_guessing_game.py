import random   # To generate random number

print("Welcome to the Number Guessing Game!!!")
print("I have selected a number between 1 and 50. can you guess it?")

# Generate random number
secret_number=random.randint(1,50)

# Initialize attempts
attempts=0

while True:
    guess=int(input("Enter your guess : "))
    attempts+=1
    
    if guess==secret_number:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
    elif guess<secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        
    if attempts==5:
        print("Game Over!!!")
        break