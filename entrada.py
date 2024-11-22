def ler_inteiro(msg = "", pos = False):
  """
    Realiza a leitura de de um valor inteiro, tratando possíveis erros

    Parâmetros:
      - msg: Mensagem a ser exibida antes da leitura. Por padrão "" (vazia)
      - pos: flag que indica a leitura apenas de um número positivo ou não. Por padrão False.

    Retorno:
     - Valor inteiro lido do teclado
  """
  while True:
    try:
      valor = int(input(msg))
      if (not pos):
        return valor
      else:
        if (valor >= 0):
          return valor
        else:
          print("Entrada de dados em formato inválido! Digite novamente:")
    except:
      print("Entrada de dados em formato inválido! Digite novamente:")


def ler_real(msg = "", pos = False):
  """
    Realiza a leitura de de um valor real, tratando possíveis erros

    Parâmetros:
      - msg: Mensagem a ser exibida antes da leitura. Por padrão "" (vazia)
      - pos: flag que indica a leitura apenas de um número positivo ou não. Por padrão False.

    Retorno:
     - Valor real lido do teclado
  """
  while True:
    try:
      valor = float(input(msg))
      if (not pos):
        return valor
      else:
        if (valor >= 0):
          return valor
        else:
          print("Entrada de dados em formato inválido! Digite novamente:")
    except:
      print("Entrada de dados em formato inválido! Digite novamente:")

def validar_string(msg = "", leng = 0):
    # Realiza a leitura de uma string, validando possível erros.
    # msg = Mensagem a ser exibida antes da leitura. Por padrão "" (vazia)
    # leng = Tamanho minímo da String a ser aceita. Por padrão 0

    while True:
      str = input(msg)
      if(len(str) >= leng): return str 
      else: print(f"A quantidade minima de caracteres deve ser {leng}")