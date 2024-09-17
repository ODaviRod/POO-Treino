class Pessoa:
    def __init__ (self):
        self.nome = "Não definido"
        self.idade = 0
        self.renda = 0.0
    def imprimir(self):
        print("Nome: ", self.nome)
        print("idade: ", self.idade)
        print("renda: ", self.renda)
    def aumento_salario(self,percent):
        self.renda = self.renda + self.renda*percent/100
    def set_dados(self,n,i,r):
        self.nome = n
        self.idade = i
        self.renda = r

pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa2.set_dados("Davi", 18, 1750.5)
print(pessoa1.imprimir())
print(pessoa2.imprimir())
pessoa2.aumento_salario(10)
print(pessoa2.renda)