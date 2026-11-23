number = 9
lives = 5
while lives >= 1:
    guess = int(input('put in your guess here :'))
    if guess == (number):
        print ('CORRECT!')
        lives = 0
    elif guess == (4,5,13,14):
        print ('cold')
        lives -= 1
    elif guess == (6,7,11,12):
        print ('warm')
        lives -= 1
    elif guess == (8,10):
        print ('HOT')
        lives -= 1
    elif guess < (4):
        print ('freezing')
    elif guess > (14):
        print ('freezing')
        lives -= 1
    for i in range (lives):
        print ('* ',end='')
if lives == 0:
    print('the number was 9!')
