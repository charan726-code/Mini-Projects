
import random
# user_num = int(input("Enter any number:"))
random_num = random.randint(1,100)
count = 5
while count >0:
    user_num = int(input("Enter any number:"))
    if user_num == random_num:
        print("correct guess..")
        break
    count-=1
    if count > 0:
        print("Wrong guess!")
        print('reamining chances:',count)

if count == 0:
    print('game over!')
    print("The correct number was:",random_num)