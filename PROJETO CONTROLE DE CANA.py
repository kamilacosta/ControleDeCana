opcao = 0
nomesFornecedores = []
nomesFuncionarios = []
nomesAutomoveis = []
placasAutomoveis = []
endereco = []
telefone = []
CNH = []
CPF = []
valorAbastecido = []
gastosManutencao = []
totalEntregue = []
data = []
hora = []
salarioFuncionario = []
while opcao != 6:
    print('*** Menu ***')
    print('[1] Cadastrar Fornecedores')
    print('[2] Cadastrar Funcionários')
    print('[3] Cadastrar Automóvel')
    print('[4] Despesas com Automóvel')
    print('[5] Entrega de Cana')
    print('[6] Sair')
    opcao= int(input('OPÇÃO: '))
    if (opcao == 1):
        print('*** Cadastrar Fornecedores***')
        entrada = 's'
        while entrada == 's':
            nomesFornecedores.append(input('Digite o nome do fornecedor: '))
            CPF.append(int(input('Digite o CPF: ')))
            endereco.append(input('Digite o endereço: '))
            telefone.append(int(input('Digite telefone: ')))
            entrada = input('Continuar? [s/n]:')
    elif(opcao == 2):
        print('*** Cadastrar Funcionários***')
        entrada = 's'
        while entrada == 's':
            nomesFuncionarios.append(input('Digite o nome do funcionário: '))
            endereco.append(input('Digite o endereço: '))
            telefone.append(int(input('Digite telefone: ')))
            CNH.append(input('Digite a CNH: '))
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 3):
        print('*** Cadastrar Automóvel***')
        entrada = 's'
        while entrada == 's':
            nomesAutomoveis.append(input('Digite o nome do automóvel: '))
            placasAutomoveis.append(input('Digite a placa do automóvel: '))
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 4):
        print('*** Despesas com Automóvel***')
        entrada = 's'
        while entrada == 's':
            valorAbastecido.append(input('Digite o valor do abastecimento: '))
            gastosManutencao.append(input('Digite o valor gasto com manutenção: '))
            salarioFuncionario.append(input('Digite salário do funcionário: '))
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 5):
        print('*** Entrega de Cana ***')
        entrada = 's'
        while entrada == 's':
            data.append(int(input('Digite a data: ')))
            hora.append(int(input('Digite a data: ')))
            CPF.append(int(input('Digite o CPF: ')))
            placasAutomoveis.append(input('Digite a placa do automóvel: '))
            totalEntregue.append(input('Digite a quantidade entregue: '))
            entrada = input('Continuar? [s/n]:')
    elif (opcao == 6):
        print('Sair')
        exit()
    else:
        print('Opção Inválida')
        entrada = input('Continuar? [s/n]:')
        if entrada == 'n':
            exit()
    
