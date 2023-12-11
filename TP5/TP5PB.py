import sched, time, subprocess, psutil

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
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
    print()
    
print ('INICIO:', time.ctime())
scheduler.enterabs(1, 3, print_event, ('primeira chamada',))
print ('CHAMADAS ESCALONADAS DA FUNÇÃO:', time.ctime(), time.process_time())

scheduler.run()
  