opcao = 0
fornecedores = []
funcionarios = []
automoveis = []
gastos = []
totalEntregue = []
while opcao != 6:
    print('*** Menu ***')
    print('[1] Cadastrar Fornecedores')
    print('[2] Cadastrar Funcionários')
    print('[3] Cadastrar Automóvel')
    print('[4] Despesas com Automóvel')
    print('[5] Entrega de Cana')
    print('[6] Imprimir listas')
    print('[7] Sair')
    opcao= int(input('OPÇÃO: '))
    if (opcao == 1):
        print('*** Cadastrar Fornecedores***')
        entrada = 's'
        while entrada == 's':
            fornecedor = input("Fornecedor: ")
            CNPJ = int(input("CNPJ: "))
            endereco = input("Endereço: ")
            telefone = int(input("Telefone: "))                          
            fornecedores.append([fornecedor, CNPJ, endereco, telefone])
            entrada = input('Continuar? [s/n]:')
    elif(opcao == 2):
        print('*** Cadastrar Funcionários***')
        entrada = 's'
        while entrada == 's':
            funcionario = input("Funcionário: ")
            endereco = input("Endereço: ")
            telefone = int(input("Telefone: "))
            CNH = int(input("Número da CNH: "))
            funcionarios.append([funcionario, endereco, telefone, CNH])
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 3):
        print('*** Cadastrar Automóvel***')
        entrada = 's'
        while entrada == 's':
            automovel = input("Automóvel: ")
            placa = input("Placa do automóvel: ")
            automoveis.append([automovel, placa])
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 4):
        print('*** Despesas com Automóvel***')
        entrada = 's'
        while entrada == 's':
            valorAbastecido = input("Valor do abastecido: ")
            gastosManutencao = input("Valor gasto com manutenção: ")
            gastos.append([valorAbastecido, gastosManutencao])
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 5):
        print('*** Entrega de Cana ***')
        entrada = 's'
        while entrada == 's':
            canaEntregue = input("Quantidade entregue: ")
            totalEntregue.append([canaEntregue])
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 6):
        print(fornecedores, funcionarios, automoveis, gastos, totalEntregue)
    elif (opcao == 7):
        print('Sair')
        exit()
    else:
        print('Opção Inválida')
        entrada = input('Continuar? [s/n]:')
        if entrada == 'n':
            exit()

#arquivo = open("fornecedores.txt", "a")
#for fornecedores in nomesFornecedores:
#    arquivo.write(%s;%s;%s\n % (fornecedor[0],fornecedor[1],fornecedor[2]))
#arquivo.close
