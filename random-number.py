import random
ran = random.randint(1,10)
a = input("hello! please enter your name! : ")
guesses = 0
print("\n hello " + a + "! please guess a number between 1 - 10. \n you have 5 chances!")

while guesses < 5:
    b = int(input())
    guesses += 1
    if guesses > ran:
        print("your guess is too high!")
    elif guesses < ran:
        print("your guess is low!")
    elif guesses == ran:
        break


if guesses == ran:
    print("you are correct! good job!! :)")

else:
    print("you are wrong!! nice try. the correct number was " , str(ran))



