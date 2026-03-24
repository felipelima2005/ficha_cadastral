op = 0
ficha = {}

while op !=4:
    print('\nFICHA CADASTRAL')
    print('1 - Incluir informações ma ficha')
    print('2 - Recuperar informações na ficha')
    print('3 - Exibir ficha completa')
    print('4 - Sair')
    op = int(input('Informe a opção desejada: '))

    if op == 1:
        #inserir dados na ficha
        chave = input('Informe o campo que vc deseja na ficha')
        valor = input('informe o valor que deseja inserir')
        #ficha[chave] = valor
        ficha.update({chave:valor})
    elif op == 2:
        #recuperar dados na ficha
        print(f'Os campos disponiveis na ficha são {ficha.keys()}')
        chave = input('informe qual campo deseja exibir: ')
        if chave in ficha.keys():
            print(ficha[chave])
        else:
            print('A chave nao existe')
       
    elif op == 3:
        #Exibir ficha completa
        print('Exibir ficha completa')
    elif op == 4:
        print('Saindo da ficha')
        break
    else:
        print('Selecione um opção valida')
