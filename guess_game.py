import random

answer = random.randint(1, 10)

def run_guess(guess, answer):

    if answer == guess:
        print('Bingo! You are a genius!')
        return 'bingo'
    else:
        print('Wrong Guess!')
        if another_try() == 'no_more_tries':
            return 'no_more_tries'
        else:
            return 'one_more_try'

def another_try():
    result = ''
    while True:
        try_again = input('Would you like to give another try? (Y/N)')
        if try_again.upper() == 'N':
            print('See you next time!')
            result = 'no_more_tries'
            break
        elif try_again.upper() == 'Y':
            result = 'Yes!'
            break
        else:
            print('Please, type (Y/N)!')
            continue
    return result

while True:
    try:
        guess = int(input('Pick a number from 1 to 10: '))
        if 1 > guess or guess > 10:
            print('The number must be between 1 and 10!')
            continue
        elif run_guess(guess, answer) == 'one_more_try':
            continue
        else:
            break

    except ValueError:
        print('Please, enter a number!')
        continue
