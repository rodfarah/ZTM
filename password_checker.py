# at least 8 characters long
# contain any sort of letters, numbers and '$%#@'
# must end with a number

import re

def create_password():

    while True:

        try:
            pattern = re.compile(r"[A-Za-z0-9$#@%#]{7,}[0-9]")
            given_passwrd = input('Type the password you want to create: ')
            check = pattern.fullmatch(given_passwrd)

            if check != None:
                print('Perfect password!!')
                break
            else:
                print(
                    'The password must be at least 8 characters long and must end with a digit! Please, try again.')
        except:
            print('Sei lá o que é o Except!')


create_password()
