while True:
    try:
        guess = int(input('Pick a number from 1 to 10: '))
        if 1 > guess or guess > 10:
            print('Erro!')
    except ValueError:
        print('Please, enter a number!')
        continue



