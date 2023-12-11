# Servidor
import socket, psutil, platform, os, time, subprocess

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    msg = socket_cliente.recv(100000)
    # Decodifica mensagem em UTF-8:
    if '$' == msg.decode('utf-8'): #Termino do cliente
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break    
    nome = msg.decode('utf-8')
    print(nome)
    lista = os.listdir()
    dic = {}
    try:
        for i in lista:
            if nome == i: #Termino do cliente
                if os.path.isfile(nome):
                    dic[nome] = []
                    dic[nome].append(os.stat(nome).st_size) # Tamanho
                    dic[nome].append(os.stat(nome).st_atime) # Tempo de criação
                    dic[nome].append(os.stat(nome).st_mtime) # Tempo de modificação
        kb = str(round(dic[nome][0]/1024, 2)) + ' KB'
        informacao = 'nome: ' + nome + '\n' + 'Tamanho: ' + kb + '\n' 
        informacao = informacao + 'Data de criação: ' + str(time.ctime(dic[nome][1])) + '\n' 
        informacao = informacao + 'Data de modificação: ' + str(time.ctime(dic[nome][2]))
        socket_cliente.send(informacao.encode('utf-8')) # Envia resposta
        print(informacao)
    except:
        pass
    try:
        pid = subprocess.Popen(nome).pid
        p = psutil.Process(pid)
        perc_mem = '{:.2f}'.format(p.memory_percent())
        mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)

        informacao_p = 'nome: ' + p.name() + '\n' + 'Executável: ' + p.exe() + '\n' 
        informacao_p = informacao_p + '\n' +  'Tempo de criação: ' + time.ctime(p.create_time()) 
        informacao_p = informacao_p + '\n' + 'Tempo de CPU de sistema: '+ str(p.cpu_times().system) + 's'
        informacao_p = informacao_p + '\n' + 'Tempo de CPU de usuário: ' + str(p.cpu_times().user) + 's'
        informacao_p = informacao_p + '\n' +'Percentual de uso de CPU: '+str(p.cpu_percent(interval = 1.0))+'%'
        informacao_p = informacao_p + '\n' + 'Percentual de uso de memória: ' + str(perc_mem) + '%'
        informacao_p = informacao_p + '\n' + 'Uso de memória: ' + str(mem) + 'MB'
        informacao_p = informacao_p + '\n' + 'Número de threads: ' + str(p.num_threads())
        socket_cliente.send(informacao_p.encode('utf-8'))
    except:
        pass
# Fecha conexão do servidor
socket_servidor.close()
input("Pressione qualquer tecla para sair...") # Espera usuário ler