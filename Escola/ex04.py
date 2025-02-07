from time import sleep
class pessoa:
    def __init__(self, nome, idade, cpf):
        
        self.nome= nome
        self.idade= idade
        self.cpf= cpf
        vivo= True

    def __str__(self):
        return f"nome: {self.nome} idade: {self.idade} cpf: {self.cpf}" 

pessoa1=pessoa("Bruce", 16, 27624897)

print(pessoa1)
