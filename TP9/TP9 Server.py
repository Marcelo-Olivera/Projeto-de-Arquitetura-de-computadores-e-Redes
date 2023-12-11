# Servidor
import socket, psutil, platform, os, time, subprocess, sched, nmap, pickle

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
    if '9' == msg.decode('utf-8'): #Termino do cliente
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    elif '1' == msg.decode('utf-8'):     
        try:
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
            bytes = pickle.dumps(lista_arq)
            socket_cliente.send(bytes) # Envia resposta
        except:
            lista = []
            lista.append('erro no servidor')
            print(lista)
            bytes = pickle.dumps(lista)
            socket_cliente.send(bytes)
    elif '2' == msg.decode('utf-8'):    
        try:
            lista = psutil.pids()
            lista_proc = []
            titulo = '{:^7}'.format("PID")
            titulo = titulo + '{:^11}'.format("# THREADS")
            titulo = titulo + '{:^26}'.format("CRIAÇÃO")
            titulo = titulo + '{:^9}'.format("T. USU.")
            titulo = titulo + '{:^9}'.format("T. SIS.")
            titulo = titulo + '{:^12}'.format("MEM. (%)")
            titulo = titulo + '{:^12}'.format("RSS")
            titulo = titulo + '{:^12}'.format("VMS")
            titulo = titulo + " EXECUTÁVEL"
            lista_proc.append(titulo)
            def mostra_info(pid):
                try:
                    p = psutil.Process(pid)
                    texto = '{:6}'.format(pid)
                    texto = texto + '{:11}'.format(p.num_threads())
                    texto = texto + " " + time.ctime(p.create_time()) + " "
                    texto = texto + '{:8.2f}'.format(p.cpu_times().user)
                    texto = texto + '{:8.2f}'.format(p.cpu_times().system)
                    texto = texto + '{:10.2f}'.format(p.memory_percent()) + " %"
                    rss = p.memory_info().rss/1024/1024
                    texto = texto + '{:10.2f}'.format(rss) + " MB"
                    vms = p.memory_info().vms/1024/1024
                    texto = texto + '{:10.2f}'.format(vms) + " MB"
                    texto = texto + " " + p.exe()
                    lista_proc.append(texto)
                except:
                    pass
            for i in lista:
                mostra_info(i)
            bytes = pickle.dumps(lista_proc)
            socket_cliente.send(bytes) # Envia resposta
        except:
            lista = []
            lista.append('erro no servidor')
            bytes = pickle.dumps(lista)
            socket_cliente.send(bytes)
    elif '3' == msg.decode('utf-8'):
        try:
            scheduler = sched.scheduler(time.time, time.sleep)
            lista_by = []

            def Long_event_1(name):
                resposta = 'INICIO DO EVENTO:' + str(time.ctime()) + str(time.process_time())
                print(resposta)
                lista_dir = []
                p_dir = ''
                nome = input()
                if os.path.isdir(nome):
                    lista_dir.append(nome)
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
                    print(nome, '\n', 'Tamanho:', str(round(somador/1024, 2)), ' KB')
                    resposta = resposta + nome + '  ' + 'Tamanho:' + str(round(somador/1024, 2)) + ' KB' + '    '
                else:
                    print("O diretório", '\''+ nome + '\'', 'não existe.')
                    resposta = resposta + "O diretório" + '\''+ nome + '\'' + 'não existe.'
                print ('FIM DO EVENTO:', time.ctime(), time.process_time())
                print()
                resposta = resposta + 'FIM DO EVENTO:' + str(time.ctime()), str(time.process_time())
                lista_by.append(resposta)

            def Long_event_2(name):
                print ('EVENTO:', time.ctime(), time.process_time())
                pid = subprocess.Popen('notepad.exe').pid

                p = psutil.Process(pid)
                resposta_2 = 'Nome: ' + p.name() + '\n' 
                resposta_2 = resposta_2 + 'Executável: ' + p.exe() + '\n'
                resposta_2 = resposta_2 + 'Data de criação: ' + str(time.ctime(p.create_time())) + '\n'
                resposta_2 = resposta_2 + 'Tempo de usuário: ' + str(p.cpu_times().user) + 's \n'
                resposta_2 = resposta_2 + 'Tempo de sistema: ' + str(p.cpu_times().system) + 's \n'
                resposta_2 = resposta_2 + 'Percentual de uso de CPU:: ' + str(p.cpu_percent(interval = 1.0)) + '% \n'
                perc_mem = '{:.2f}'.format(p.memory_percent())
                resposta_2 = resposta_2 + 'Percentual de uso de memória: ' + perc_mem + '% \n'
                mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
                resposta_2 = resposta_2 + 'Uso de memória: ' + mem + 'MB \n'
                resposta_2 = resposta_2 + 'Número de threads: ' + str(p.num_threads()) + '\n'
                resposta_2 = resposta_2 + 'FIM DO EVENTO:' + str(time.ctime()) + ' clock: ' + str(time.process_time())
                print(resposta_2)
                lista_by.append(resposta_2)
                print()
    
            inicio = 'INICIO:' + str(time.ctime())
            lista_by.append(inicio)
            print(inicio)
            scheduler.enter(2, 3, Long_event_1, ('TAMANHO DE DIRETÓRIOS',))
            scheduler.enter(8, 1, Long_event_2, ('LISTA DE INFORMAÇÕES DE UM PROCESSO',))
            chamada = 'CHAMADAS ESCALONADAS DA FUNÇÃO:'+ str(time.ctime()) + str(time.process_time())
            print(chamada)
            scheduler.run()
            lista_by.append(chamada)
            bytes = pickle.dumps(lista_by)
            socket_cliente.send(bytes)
        except:
            lista = []
            lista.append('erro no servidor')
            bytes = pickle.dumps(lista)
            socket_cliente.send(bytes)
    
    elif '4' == msg.decode('utf-8'):
        msg = 'Ok... Entre com um IP alvo(o processo pode levar alguns minutos): '
        socket_cliente.send(msg.encode('utf-8'))
        msg = socket_cliente.recv(100000)
        def obter_hostnames(host_validos):
            resposta = "O teste foi feito na sub rede: " + base_ip + '\n'
            resposta = resposta + "Os hosts válidos são: " + str(host_validos) + '\n'
            nm = nmap.PortScanner()
            for i in host_validos:
                try:
                    nm.scan(i)
                    resposta = resposta + '\n' + 'O IP possui o nome ' + str(nm[i].hostname()) + '\n'
                    
                    for proto in nm[i].all_protocols():
                        resposta = resposta + '----------' + '\n'
                        resposta = resposta + 'Protocolo : ' + proto + '\n'

                        lport = nm[i][proto].keys()
                
                        for port in lport:
                            resposta = resposta + 'Porta: ' + str(port) + '    ' + 'Estado: '  +  str(nm[i][proto][port]['state']) + '\n'
                    msg = 'O endereço IP' + str(i) + 'foi verificado'
                    print(msg)
                    print(resposta)
                except:
                    resposta = resposta + 'O IP deu problema.'
                    pass
                
            lis.append(resposta)

        def retorna_codigo_ping(hostname):
            """Usa o utilitario ping do sistema operacional para encontrar   o host. ('-c 5') indica, em sistemas linux, que deve mandar 5   pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3   milisegundos por uma resposta. Esta funcao retorna o codigo de   resposta do ping """
    
            plataforma = platform.system()
            args = []
            if plataforma == "Windows":
                args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]
  
            else:
                args = ['ping', '-c', '1', '-W', '1', hostname]
        
            ret_cod = subprocess.call(args,
                                        stdout=open(os.devnull, 'w'),
                                        stderr=open(os.devnull, 'w'))
            return ret_cod

        def verifica_hosts(base_ip):
            """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
            print("Mapeando\r")
            host_validos = []
            return_codes = dict()
            for i in range(1, 255):
        
                return_codes[base_ip + '{0}'.format(i)] =   retorna_codigo_ping(base_ip + '{0}'.format(i))
                if i %20 ==0:
                    print(".", end = "")
                if        return_codes[base_ip + '{0}'.format(i)] == 0:
                    host_validos.append(base_ip + '{0}'.format(i))
            print("\nMapping ready...")
    
            return host_validos
        # Chamadas 
        lis = []
        ip_string = msg.decode('utf-8')
        ip_lista = ip_string.split('.')
        base_ip = ".".join(ip_lista[0:3]) + '.'
        print("O teste será feito na sub rede: ", base_ip)
        host_validos = verifica_hosts(base_ip)
        print ("Os host válidos são: ", host_validos)

        print('Iniciando nmap.PortScanner')
        obter_hostnames(host_validos)
        print()
        print('FIM.')
        bytes = pickle.dumps(lis)
        socket_cliente.send(bytes)

    elif '5' == msg.decode('utf-8'):
        interfaces = psutil.net_if_addrs()
        nomes = []
        lista = []
        # Obtém os nomes das interfaces primeiro
        for i in interfaces:
            nomes.append(str(i))
        # Depois, imprimir os valores:
        for i in nomes:
            resposta = str(i)+ ":" + '\n'
            for j in interfaces[i]:
                resposta = resposta + str(j) + '\n'
            resposta = resposta + '----------------------------------------------------------------'
            lista.append(resposta)
        bytes = pickle.dumps(lista)
        socket_cliente.send(bytes)

# Fecha conexão do servidor
socket_servidor.close()
input("Pressione qualquer tecla para sair...") # Espera usuário ler