from entrada import *
from gerenciadorJSON import *

# Coleta os dados de um aluno, e os armazena em forma de dicionário
def cadastro_aluno(id):
    nome = input("Informe o nome do aluno: ")
    contato = input("Infome seu e-mail: ")
    idade = ler_inteiro("Informe a idade do aluno: ", True)
    peso = ler_real("Informe o peso do aluno: ", True)
    altura = ler_real("Informe a altura: ", True)

    aluno = {
        "id": id,
        "nome": nome ,
        "contato": contato,
        "idade":  idade,
        "peso": peso,
        "altura": altura,
        "IMC": round((peso / altura), 2)

    }
    print(aluno)
    return aluno


def salvar_alunos(novos_alunos):
    alunos_salvos = buscar_todos_alunos_em_arquivo() # Busca se já existem alunos salvos
    alunos = alunos_salvos + novos_alunos # Junta os alunos antigos com os novos
    salvar_alunos_em_arquivo(alunos)
