import os
import json

FILE_PATH = 'data.json'

def criar_arquivos_armazenador(): open(FILE_PATH, 'w') # Cria arquivo que armazena informações sobre os alunos

def buscar_todos_alunos_em_arquivo(): # Busca no arquivo data.json , se ja existem dados 
    try:
        with open(FILE_PATH, 'r') as file:
            alunos = json.load(file) # Se sim , retorna alunos
            return alunos
    except: 
        print("ERRO AO BUSCAR")
        return [] # Se não, uma lista vazia

def salvar_alunos_em_arquivo(novos_alunos):
    alunos_salvos = buscar_todos_alunos_em_arquivo()
    try:
        with open(FILE_PATH, 'w') as file:
            alunos = json.dumps(alunos_salvos + novos_alunos)
            file.write(alunos)
            print("DADOS SALVOS COM SUCESSO")
    except Exception as error:
        print("ERRO: ", + error)
