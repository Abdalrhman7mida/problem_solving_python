print('think of a number between 0 to 100, and we will get it right fast !')
low = 0
high = 100
medium = (low + high) / 2
state = True
while state:
    print('Is your number ' + str(medium))
    guess = input('Enter h to indicate the guess is too high, l to indicate is too low, c to indicate it\'s correct: ')
    if guess == 'c':
        print('game over, your secrete number = '+ str(medium))
        state = False
    elif guess == 'h':
        high = medium
        medium = (high + low) // 2
    elif guess == 'l':
        low = medium
        medium = (high + low) // 2
    else:
        print('i didn\' understand your input.')
