import os, time
# Obtém lista de arquivos e diretórios do diretório corrente:
lista = os.listdir()
dic = {} # cria dicionário
lista_arq = []
for i in lista: # Varia na lista dos arquivos e diretórios
    if os.path.isfile(i): # checa se é um arquivo
        # Cria uma lista para cada arquivo. Esta lista contém o
        # tamanho, data de criação e data de modificação.
        dic[i] = []
        dic[i].append(os.stat(i).st_size) # Tamanho
        dic[i].append(os.stat(i).st_atime) # Tempo de criação
        dic[i].append(os.stat(i).st_mtime) # Tempo de modificação

titulo = '{:11}'.format("Tamanho") # 10 caracteres + 1 de espaço
# Concatenar com 25 caracteres + 2 de espaços
titulo = titulo + '{:27}'.format("Data de Modificação")
# Concatenar com 25 caracteres + 2 de espaços
titulo = titulo + '{:27}'.format("Data de Criação")
titulo = titulo + "Nome"
lista_arq.append(titulo)
for i in dic:
    kb = dic[i][0]/1024
    tamanho = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))
    arquivo = tamanho + str(time.ctime(dic[i][2])) + " " + str(time.ctime(dic[i][1])) + " " + i
    lista_arq.append(arquivo)

for i in range(len(lista_arq)):
    print(lista_arq[i])
    