import random

answer = random.randint(1,10)

def another_try():
    result = ''
    while True:
        try_again = input('Would you like to give another shot? (Y/N)')
        if try_again.upper() == 'N':
            print('See you next time!')
            result = 'Stop!'
            break
        elif try_again.upper() == 'Y':
            result = 'Try Again!'
            break
        else:
            print('Please, type (Y/N)!')
            continue

    return result


while True:
    try:
        guess = int(input('Pick a number from 1 to 10: '))
        print(answer)
        if 1 > guess > 10:
            print('Please, you must choose a number between 1 and 10! ')
            continue
        if answer == guess:
            print('Bingo')
            break
        else:
            print('Wrong Pick!')
            if another_try() == 'Stop!':
                break
            else:
                continue
    except ValueError:
        print('Please, enter a number!')
        continue
