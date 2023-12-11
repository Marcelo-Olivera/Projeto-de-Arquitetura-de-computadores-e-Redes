# Cliente
import socket, sys
# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Tenta se conectar ao servidor
    s.connect(("192.168.0.59", 9999))
   
except Exception as erro:
    print(str(erro))
    sys.exit(1) # Termina o programa

opcao = input('O que você deseja? ')
while 'lista de informações de arquivos e diretórios' == opcao:
    print("Para encerrar, digite '$'")
    msg = input('digite o nome do arquivo: ')
    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('utf-8'))
    msg = s.recv(100000)
    print(msg.decode('utf-8')) #.decode('utf-8')
    opcao = input('O que você deseja? ')
    
while 'lista de informação de processo' == opcao:
    print("Para encerrar, digite '$'")
    msg = input('digite o nome do processo: ')
    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('utf-8'))
    msg = s.recv(100000)
    print(msg.decode('utf-8')) #.decode('utf-8')
    opcao = input('O que você deseja? ')
     
if msg == '$':
    # Fecha conexão com o servidor
    s.close()
else:
    print('não esxiste essa opção!')
    opcao = input('O que você deseja? ')


