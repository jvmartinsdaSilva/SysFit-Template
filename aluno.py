from entrada import *

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


