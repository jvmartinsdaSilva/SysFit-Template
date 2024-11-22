from aluno import *
from entrada import *
from navegabilidade import *
from gerenciadorJSON import *

#variáveis de controle dos dados na memória
id = buscar_id_ultimo_aluno(buscar_todos_alunos_em_arquivo())
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
    if (opc == 1): #Função para cadastro de alunos
        aluno = cadastro_aluno(id)
        alunos.append(aluno)
        id += 1
        pass
    elif (opc == 2): # Mostra todos alunos na tela
        mostrar_alunos(buscar_todos_alunos_em_arquivo())
        pass
    elif (opc == 3): #busca um aluno por id e apresenta seus dados se existir
        aluno = buscar_aluno_por_id(buscar_todos_alunos_em_arquivo() + alunos)
        print(aluno)
        pass
    elif (opc == 4): #exibe uma lista com todos os alunos filtrados por imc
        aluno = buscar_aluno_por_IMC(buscar_todos_alunos_em_arquivo() + alunos)
        print(aluno)
        pass
    elif (opc == 5):
        salvar_alunos(alunos)
        break
    else:
        print("Opção inválida!")

    limpar_tela()
