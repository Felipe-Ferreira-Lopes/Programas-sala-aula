dicionario = {i: i ** 2 for i in range(0, 100)if i % 2 == 0}
for chave, valor in dicionario.items():
    print("numero: {}, quadrado: {}".format(chave, valor))