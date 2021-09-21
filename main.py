### Libs ###

import csv
from datetime import datetime, timedelta
import string

### Listas ###

arquivo_cru = []
arquivo_tratado =[]

### Funções ###

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

### Tratamento ###

with open("dados_pessoais.csv", "r") as dados:
    arquivo_ler = csv.DictReader(dados, delimiter=";")
    for dicionario in arquivo_ler:        
        arquivo_cru.append({
        "nome": dicionario.get("nome"),
        "data de nascimento": dicionario.get("data_nascimento").replace("-","/"),
        "altura": dicionario.get("altura").replace(",","."),
        "peso": dicionario.get("peso").replace(",","."),   
        })

for linha in arquivo_cru:
    try:      
        if len(linha.get("data de nascimento").split("/")[2]) == 2:
          data_nascimento_calc = datetime.strptime(linha.get("data de nascimento"), "%d/%m/%y")
          data_nascimento = datetime.strptime(linha.get("data de nascimento"), "%d/%m/%y").strftime("%d/%m/%Y")
        elif len(linha.get("data de nascimento").split("/")[2]) == 4:
            data_nascimento_calc = datetime.strptime(linha.get("data de nascimento"), "%d/%m/%Y")
            data_nascimento = datetime.strptime(linha.get("data de nascimento"), "%d/%m/%Y").strftime("%d/%m/%Y")
    except IndexError:
        data_nascimento_calc = ("Dados insuficientes")
        data_nascimento = ("Dados insuficientes")

    nome = string.capwords(linha.get("nome"))
    idade = idade_calc(data_nascimento_calc)
    altura = "{:.2f}".format(float(linha.get("altura")))
    peso = "{:.1f}".format(float(linha.get("peso")))
    imc = imc_calc(peso, altura)    
        
    arquivo_tratado.append({
        "nome": nome,
        "data de nascimento": data_nascimento,
        "idade": idade,
        "altura": altura,
        "peso": peso,
        "imc": imc,
    })

### Conversão ###

dados_tratados = "dados_tratados.csv"
colunas_dados = ["nome", "data de nascimento", "idade", "altura", "peso", "imc"]
with open(dados_tratados, 'w') as arquivo:
        atualizar = csv.DictWriter(arquivo, delimiter=";", fieldnames = colunas_dados)
        atualizar.writeheader()
        for data in arquivo_tratado:
            atualizar.writerow(data)
arquivo.close()
