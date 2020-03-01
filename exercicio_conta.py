from conta import Conta, Cliente, Data, Historico

data1 = Data("01", "janeiro", 2020)
data2 = Data("02", "janeiro", 2020)

cliente1 = Cliente("felipe", "ferreira", 123456789)
cliente2 = Cliente("alisson", "saraiva", 987654321)

conta1 = Conta("123-4", cliente1, 200, 1000, data1)
conta2 = Conta("123-5", cliente2, 150, 3000, data2)

conta1.depositar(50)
conta1.sacar(30)
conta1.transferir(conta2,20)
conta1.extrato()


conta2.depositar(80)
conta2.sacar(40)
conta2.extrato()
conta1.historico.imprimir()