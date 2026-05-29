# 1. Number guessing game
#    → computer picks random number 1-100
#    → user guesses, hints too high too low
#    → count attempts, show score
import random


def numberGame():
 randomNum = random.randint(1, 100)
 user_guess = 0
 count = 0
 while user_guess != randomNum:
  count += 1
  user_guess = int(input("Guess the number!"))
  if user_guess > randomNum:
   print("your number is greater, guess the lesser number")
  elif user_guess < randomNum:
   print("your number is smaller then the expected number")  
  else:
   return print(f"yay! you guessed {randomNum} in {count} attempts")
  if count == 5:
   return print(f"out of attempts! the number was {randomNum}")
  
  
while True:
 numberGame()
 
 choice = input("Play again! [y,n]").lower()
 if choice != "y":
  break
 


 

