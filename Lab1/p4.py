from random import*
answer = randint(1,50)

correct = False 

while correct == False:
    num = input('Please input your guess between 1 and 50: ')
    if num == answer:
        correct = True
    elif num < answer:
        print 'Too low!'
    elif num > answer:
        print 'Too high!'
    
print 'You are right!'
