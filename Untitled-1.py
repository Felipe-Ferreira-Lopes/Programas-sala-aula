with open('pessoas') as arquivo:
    with open("sapato.txt", 'w') as saida:
        for linha in arquivo:
            print("Nome: {}, Idade: {}",format(*linha.strip("\n").split(',')))

if arquivo.closed:
    print("arquivo esta fechado")