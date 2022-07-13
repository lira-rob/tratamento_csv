from datetime import datetime, timedelta

def imc_calc (peso, altura):
    try:
        if peso and altura:
          imc = float(peso) / float(altura)**2
          return int(imc)
    except ValueError:
      imc = "Dados insuficientes"
      return imc

def idade_calc (nascimento):
      try:
          idade = (datetime.now() - nascimento) // timedelta(days=365.2425)
          return idade
      except TypeError:
          idade = ("Dados insuficientes")
          return idade