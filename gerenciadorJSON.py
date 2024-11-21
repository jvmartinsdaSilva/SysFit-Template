import os
import json

FILE_PATH = 'data.json'

def criar_arquivos_armazenador(): open(FILE_PATH, 'w') # Cria arquivo que armazena informações sobre os alunos

def buscar_todos_alunos_em_arquivo(): # Busca no arquivo FILE_PATH , se ja existem dados 
    try:
        with open(FILE_PATH, 'r') as file:
            alunos = json.load(file) # Se sim , retorna uma lista de alunos
            return alunos
    except: 
        return [] # Se não, uma lista vazia


def salvar_alunos_em_arquivo(alunos): # Recebe alunos que serão salvos em arquivo
    try:
        with open(FILE_PATH, 'w') as file:
            file.write(json.dumps(alunos)) #Transforma os dados em JSON e os salva no arquivo
            print("DADOS SALVOS COM SUCESSO")
    except Exception as error:
        print("ERRO: ", + error)
