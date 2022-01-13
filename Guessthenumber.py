import random
number = random.randint(0,100)
A = 0
while A < 6:
    guess = int(input())
    A = A + 1

    if guess < number:
       print("The number is too low")
    
    if guess > number:
       print("The number is too high")

    if guess == number:
       print("Correct, you are too good!")
       break
    
    if A >= 6:
       print("Game over")

print("The correct answer is",(number))             