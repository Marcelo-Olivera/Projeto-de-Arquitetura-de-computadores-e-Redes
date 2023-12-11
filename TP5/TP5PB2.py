import sched, time, os, psutil, subprocess

scheduler = sched.scheduler(time.time, time.sleep)

def Long_event_1(name):
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
        print('tamanho: ' + str(round(somador/1024, 2)) + ' KB')
    else:
        print("O diretório", '\''+ entrada + '\'', 'não existe.')
    print ('FIM DO EVENTO:', time.ctime(), time.process_time())
    print()
      
def Long_event_2(name):
    print ('EVENTO:', time.ctime(), time.process_time(), name)
    pid = subprocess.Popen('notepad.exe').pid

    p = psutil.Process(pid)
    print('Nome: ', p.name())
    print('Executável: ', p.exe())
    print('Tempo de criação: ', time.ctime(p.create_time()))
    print('Tempo de usuário: ', p.cpu_times().user, 's')
    print('Tempo de sistema: ', p.cpu_times().system, 's')
    print('Percentual de uso de CPU:: ', p.cpu_percent(interval = 1.0), '%')
    perc_mem = '{:.2f}'.format(p.memory_percent())
    print('Percentual de uso de memória: ', perc_mem, '%')
    mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
    print('Uso de memória: ', mem, 'MB')
    print('Número de threads: ', p.num_threads())
    print ('FIM DO EVENTO:', time.ctime(), time.process_time())
    print()
    
print('INICIO:', time.ctime())
scheduler.enter(2, 3, Long_event_1, ('LISTA DE INFORMAÇÕES DE ARQUIVOS E DIRETÓRIOS',))
scheduler.enter(8, 2, Long_event_2, ('LISTA DE INFORAÇÕES DE UM PROCESSO',))
print('CHAMADAS ESCALONADAS DA FUNÇÃO:', time.ctime(), time.process_time())

scheduler.run()