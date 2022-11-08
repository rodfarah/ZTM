class Estudante:
    nome = 'Sei lá'
    idade = 22

fulano = Estudante()

setattr(fulano, 'idade', 34)


print(fulano.idade)