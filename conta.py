import datetime

class Historico:
    def __init__(self):
        self.data_de_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprimir(self):
        print("Data de abertura: {}".format(self.data_de_abertura))
        for x in self.transacoes:
            print("",x)
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    


class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.historico = Historico()
    
    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depositou: {}".format(valor))
    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("sacou: {}".format(valor))
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {} \nnome: {} \ndata: {}/{}/{}".format(self.numero, self.saldo, self.titular.nome, self.data_abertura.dia, self.data_abertura.mes, self.data_abertura.ano))

    def transferir(self, destino, valor):
        retirou = self.sacar(valor)
        if (retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("transferiu: {}".format(valor))
            return True 