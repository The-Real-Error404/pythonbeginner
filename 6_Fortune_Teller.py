import random

answers = ["Of course!","No way!","Probably!","Probably not.","I'm too tired to answer.", "Ask again later.", "That's not very likely.","I think so.","Who knows?"]
print("Hi! I'm Predicta, the computer fortune teller! ")

while True:
    print("What would you like me to predict?")
    question = input()

    if question == "quit":
        break
    
    response = random.choice(answers)  #answers[0]  
    print(response)

print("Bye!")
    
    
