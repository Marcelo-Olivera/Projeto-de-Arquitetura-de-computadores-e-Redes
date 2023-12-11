import os
lista_dir = []
p_dir = ''
entrada = input()
if os.path.isdir(entrada):
    lista_dir.append(entrada)
    somador = 0
    while lista_dir:
        diretorio = lista_dir[0]
        p_dir = os.path.join(p_dir, diretorio)
        lista = os.listdir(p_dir)
        for i in lista:
            p = os.path.join(p_dir, i)
            if os.path.isdir(p):
                lista_dir.append(i)
            elif os.path.isfile(p):
                somador = somador + os.stat(p).st_size
        lista_dir.remove(diretorio)
    print(str(round(somador/1024, 2)) + ' KB')
else:
    print("O diretório", '\''+ entrada + '\'', 'não existe.')
    