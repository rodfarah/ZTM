# Given the below class:
class Cat:
    '''
    Instanciates cats
    '''
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Fulano', 12)
cat2 = Cat('Beltrano', 7)
cat3 = Cat('Ciclano', 9)

# 2 Create a function that finds the oldest cat

def get_oldest_cat(*args):
    return max(args)

print(f'O gato mais velho tem {get_oldest_cat(cat1.age, cat2.age, cat3.age)} anos de idade')


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
