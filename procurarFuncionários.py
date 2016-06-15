import os

arquivo_listaFuncionarios = "funcionarios.txt"

def gravar_funcionarios(listaFunconarios):
    arq = open(arquivo_listaFuncionarios, "a")
    arq.write(%s,%s,%s/n" % (funcionarios[0],funcionarios[1],funcionarios[2]))
    arq.close()

def ler_funcionarios():
    funcionarios = []
    if not os.path.exists(arquivo_listaFuncionarios):
        return funcionarios
    
    arq = open(arquivo_listaFuncionarios,"r")
    linhas = arq.read().splitlines()
    for linha in linhas:
        funcionarios_str = linha.split(";")
        endereco = funcionarios_str[0]
        telefone = funcionarios_str[1]
        CNH = funcionarios_str[2]
        funcionarios.append([endereco, telenone, CNH])
    return funcionarios

def existe_funcionario(funcionarios):
    return funcionario in ler_funcionarios()
