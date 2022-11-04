import random

answer = random.randint(1,10)

while True:
    try:
        guess = int(input('Pick a number from 1 to 10: '))
        print(answer)
        if 1 <= guess <= 10:
            if answer == guess:
                print('Bingo')
                break
            else:
                print('Wrong Pick!')
                try_again = input('Would you like to try again? ')
                if try_again.upper() == 'N':
                    print('Até a próxima!')
                    break
                elif try_again.upper() == 'Y':
                    continue
                # else:
                #     print('Please, type Yes or No (Y/N)!')
                #     continue
        else:
            print('Eu disse de 1 a 10! ')
    except ValueError:
        print('Please, enter a number!')
        continue
    except try_again.upper() != 'Y' and try_again.upper() != 'N':
        print('Please, type Yes or No (Y/N)!')