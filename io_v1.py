arquivo = open('pessoas.csv')
dados = arquivo.read()

for linha in dados.splitlines()
	print("nome: {}, idade: {}",format(*linha, split(' , ')))


arquivo.close()