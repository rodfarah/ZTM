class Aluno():
    def matriculado(self):
        print('Matrícula Feita!')


class Turma_Um(Aluno):
    def __init__(self, nome, media):
        self.nome = nome
        self.media = media

    def situacao(self):
        if self.media >= 7:
            print(
                f'O aluno {self.nome} foi aprovado com uma nota média de {self.media}')
        else:
            print(
                f'O aluno {self.nome} foi reprovado com uma nota média de {self.media}')


class Turma_Dois(Aluno):
    def __init__(self, nome, presença):
        self.nome = nome
        self.presença = presença

    def situacao(self):
        if self.presença >= 70:
            print(
                f'O aluno {self.nome} foi aprovado com uma presença de {self.presença} por cento')
        else:
            print(
                f'O aluno {self.nome} foi reprovado com uma presença de {self.presença} por cento')


aluno1 = Turma_Um('Pedro', 10)
aluno2 = Turma_Dois('Pablo', 70)
aluno3 = Turma_Um('Ana Maria', 6)
aluno4 = Aluno()


aluno2.situacao() #1
aluno1.situacao() #2
aluno3.situacao() #3
aluno4.matriculado() #4

print(isinstance(aluno1, Turma_Dois)) #5
print(isinstance(aluno2, Turma_Dois)) #6
print(isinstance(aluno1, Aluno)) #7