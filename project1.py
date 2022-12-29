import random 
value = True
score = 0
while value:
    num = int(input('Enter your value b/w 1 to 6: '))
    if num >= 1 and num <= 6:
        rand = random.randint(1,6)
        print(f'Random value is : {rand}')
        print(f'Your value is :{num}')
        if (num == rand):
            print('YOU WON')
            score = score+1
            print(score)
        else:
            print('YOU LOST')
            print(score-score)
        t = input('want to roll the dice again? (y/n): ')
        if t.lower() == "y":
            continue
        elif t.lower()=="n":
            print("Thanks for playing!!!")
            break
        else:
            print("Bruhh...Type 'y' or 'n' ")
    else:
        print("Bruhh...Type the number between 1 to 6 🤦🏼‍♀️️")


    
 

 

 