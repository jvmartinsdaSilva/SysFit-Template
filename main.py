from aluno import *
from entrada import *
from navegabilidade import *
from gerenciadorJSON import *

#variáveis de controle dos dados na memória
id = 1
""" número do id de autoincremento
"""
alunos = []
""" lista de dicionários que armazena as abstrações de alunos
"""

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")
    #navegabilidade
    if (opc == 1):
        aluno = cadastro_aluno(id)
        alunos.append(aluno)
        id += 1
        pass
    elif (opc == 2):
        #função imprime todos os alunos em tela
        pass
    elif (opc == 3):
        #busca um aluno por id e apresenta seus dados se existir
        pass
    elif (opc == 4):
        #exibe uma lista com todos os alunos filtrados por imc
        pass
    elif (opc == 5):
        salvar_alunos_em_arquivo(alunos)
        break
    else:
        print("Opção inválida!")

    limpar_tela()
