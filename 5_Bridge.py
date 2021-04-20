import random

def play():
    print("You are walking in an ice storm back to camp.")
    print("You see 3 ice bridges ahead. They look dangerous.")
    alive = True
    score = 0
    while alive:
        number = random.randint(1,3)
        print("Choose bridge 1, 2, or 3.")
        guess = int(input())

        if guess < 1 or guess > 3:
            print("Invalid Bridge! Try Again") 
            
        elif guess == number:
            print("Crack -- Crash -- Bye, byeeeeeeeeeeeeeeeeeeee!")
            alive = False
        else:
            print("Nice job! You are safe for now...")
            print("There are more bridges ahead.")
            score += 1

    print(" Game Over! You scored " + (str)(score) + ".")

play()
