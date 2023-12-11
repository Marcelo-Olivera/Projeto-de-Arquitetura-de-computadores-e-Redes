# Cliente
import socket, sys, pickle
# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Tenta se conectar ao servidor
    s.connect(("192.168.0.129", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1) # Termina o programa
msg = input("Menu: \n [1] Informações de arquivos e diretórios \n [2] Informações de processo \n [3] Escalonamento de Chamadas \n [4] Redes e Subredes \n [5] Informação de interfaces de rede \n [9] Sair \n")
                    # Envia mensagem codificada em bytes ao servidor
s.send(msg.encode('utf-8'))
while msg != '9':
    if msg == '1':
        bytes = s.recv(10000)
        lista_arq = pickle.loads(bytes)
        for i in range(len(lista_arq)):
            print(lista_arq[i])
        msg = input("Menu: \n [1] Informações de arquivos e diretórios \n [2] Informações de processo \n [3] Escalonamento de Chamadas \n [4] Redes e Subredes \n [5] Informação de interfaces de rede \n [9] Sair \n")
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('utf-8'))
    if msg == '2':
        bytes = s.recv(100000)
        lista_proc = pickle.loads(bytes)
        for i in range(len(lista_proc)):
            print(lista_proc[i])
        msg = input("Menu: \n [1] Informações de arquivos e diretórios \n [2] Informações de processo \n [3] Escalonamento de Chamadas \n [4] Redes e Subredes \n [5] Informação de interfaces de rede \n [9] Sair \n")
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('utf-8'))
    if msg == '3':
        bytes = s.recv(100000)
        lista_esc = pickle.loads(bytes)
        for i in range(len(lista_esc)):
            print(lista_esc[i])
        msg = input("Menu: \n [1] Informações de arquivos e diretórios \n [2] Informações de processo \n [3] Escalonamento de Chamadas \n [4] Redes e Subredes \n [5] Informação de interfaces de rede \n [9] Sair \n")
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('utf-8'))
    if msg == '4':
        bytes = s.recv(100000)
        if 'Ok... Entre com um IP alvo(o processo pode levar alguns minutos): ' == bytes.decode('utf-8'):
            print(bytes)
            msg = input()
            s.send(msg.encode('utf-8'))
            bytes = s.recv(100000)
            lista_proc = pickle.loads(bytes)
            for i in range(len(lista_proc)):
                print(lista_proc[i])
            msg = input("Menu: \n [1] Informações de arquivos e diretórios \n [2] Informações de processo \n [3] Escalonamento de Chamadas \n [4] Redes e Subredes \n [5] Informação de interfaces de rede \n [9] Sair \n")
            # Envia mensagem codificada em bytes ao servidor
            s.send(msg.encode('utf-8'))
    if msg == '5':
        bytes = s.recv(100000)
        lista_ir = pickle.loads(bytes)
        for i in range(len(lista_ir)):
            print(lista_ir[i])
        msg = input("Menu: \n [1] Informações de arquivos e diretórios \n [2] Informações de processo \n [3] Escalonamento de Chamadas \n [4] Redes e Subredes \n [5] Informação de interfaces de rede \n [9] Sair \n")
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('utf-8'))
# Fecha conexão com o servidor
s.close()
