arquivo = open('pessoas.csv')

try:
	print("Entrei no try")
	for linha in arquivo:
		print("nome: {}, idade: {}".format(*linha.strip('\n').split(',')))

finally:
	arquivo.close()
	print("Entrei no finally")


print("estou no fim do codigo")