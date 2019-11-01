arquivo_amazon = open('amazon.csv')

try:
	print("Entrei no try")
	for linha in arquivo_amazon:
		print("Ano: {}, Estado: {}, mes: {}, numero {}, data: {}".format(*linha.strip('\n').split(',')))

finally:
	arquivo_amazon.close()
	print("Entrei no finally")


print("estou no fim do codigo")