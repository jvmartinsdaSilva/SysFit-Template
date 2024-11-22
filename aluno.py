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

def mostrar_alunos(alunos):
    for aluno in alunos:
        print(aluno)

def salvar_alunos(alunos):
    alunos_salvos = buscar_todos_alunos_em_arquivo() # Busca se já existem alunos salvos
    novos_alunos = alunos_salvos + alunos # Junta os alunos antigos com os novos
    salvar_alunos_em_arquivo(novos_alunos)

def buscar_aluno_por_id(alunos):
    id = ler_inteiro("Informe o Id do aluno desejado: ", True)
    for aluno in alunos:
        if(aluno['id'] == id): return aluno
    return f"Aluno com o id: {id} não encontrado"
    

def buscar_aluno_por_IMC(alunos):
    imc = ler_real("Informe o valor do IMC desejado", True)
    for aluno in alunos:
        if(aluno['IMC'] == imc): return aluno
    return f"Aluno com o IMC: {imc} não encontrado"


def buscar_id_ultimo_aluno(alunos):
    try:
        ultimo_aluno = alunos[-1]
        return (ultimo_aluno['id'] + 1) #Se Houver alunos , retorna o id do ultimo aluno + 1 (Próximo id)
    except:
        return 1 #Se não houver alunos salvos , retorna 1 (Primeiro Aluno)