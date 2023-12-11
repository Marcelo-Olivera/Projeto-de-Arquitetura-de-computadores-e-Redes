import pygame, psutil, platform, cpuinfo

  # Iniciando a janela principal
largura_tela = 1200
altura_tela = 720
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Monitoramento e análise do computador")
pygame.display.init()
info_cpu = cpuinfo.get_cpu_info()
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
preto = (0,0,0)
branco = (255,255,255)
cinza = (100, 100, 100)
s1 = pygame.surface.Surface((largura_tela, altura_tela/3))
s2 = pygame.surface.Surface((largura_tela, altura_tela/3))
s3 = pygame.surface.Surface((largura_tela, altura_tela/3))

pygame.font.init()
font = pygame.font.Font(None, 22)

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    perc = mem.percent
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(s1, azul, (20, 60, larg, 70))
    tela.blit(s1, (0, 0))
    larg = larg*mem.percent/100
    pygame.draw.rect(s1, vermelho, (20, 60, larg, 70))
    tela.blit(s1, (0, 0))
    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB): " + str(perc) + "%"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10)) 
    
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    pygame.draw.rect(s2, azul, (20, 50, larg, 70))
    tela.blit(s2, (0, altura_tela/4))
    larg = larg*capacidade/100
    pygame.draw.rect(s2, vermelho, (20, 50, larg, 70))
    tela.blit(s2, (0, altura_tela/4))
    texto_barra_2 = "Uso da CPU: " + str(capacidade) + "%"
    text2 = font.render(texto_barra_2, 1, branco)
    tela.blit(text2, (20, altura_tela/4))
    texto_proc = str(platform.processor())
    textp = font.render(texto_proc, 1, branco)
    tela.blit(textp, (20, altura_tela/4 + 125))
    texto_node = str(platform.node())
    textn = font.render(texto_node, 1, branco)
    tela.blit(textn, (20, altura_tela/4 + 140))
    texto_plat = str(platform.platform())
    textpl = font.render(texto_plat, 1, branco)
    tela.blit(textpl, (20, altura_tela/4 + 155))
    texto_sistema = str(platform.system())
    texts = font.render(texto_sistema, 1, branco)
    tela.blit(texts, (20, altura_tela/4 + 170))
    texto_nome = "Nome: " + str(info_cpu["brand_raw"])
    textnm = font.render(texto_nome, 1, branco)
    tela.blit(textnm, (450, altura_tela/4 + 125))
    texto_arq = "Arquitetura: " + str(info_cpu["arch"])
    textar = font.render(texto_arq, 1, branco)
    tela.blit(textar, (450, altura_tela/4 + 140))
    texto_palavra = "Palavra (bits): " + str(info_cpu["bits"])
    textpa = font.render(texto_palavra, 1, branco)
    tela.blit(textpa, (450, altura_tela/4 + 155))
    texto_freq = "Frequência (MHz):" + str(round(psutil.cpu_freq().current))
    textfr = font.render(texto_freq, 1, branco)
    tela.blit(textfr, (450, altura_tela/4 + 170))
    texto_nucleos = "Núcleos (físicos):" + str(psutil.cpu_count()) + " (" + str(psutil.cpu_count(logical=False)) + ")"
    textnu = font.render(texto_nucleos, 1, branco)
    tela.blit(textnu, (450, altura_tela/4 + 185))
    
def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    pygame.draw.rect(s3, azul, (20, 50, larg, 70))
    tela.blit(s3, (0, 6*altura_tela/10 - 50))
    larg = larg*disco.percent/100
    pygame.draw.rect(s3, vermelho, (20, 50, larg, 70))
    tela.blit(s3, (0, 6*altura_tela/10 - 50))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra_3 = "Uso de Disco: (Total: " + str(total) + "GB): " + str(disco.percent) + "%"
    text3 = font.render(texto_barra_3, 1, branco)
    tela.blit(text3, (20,  6*altura_tela/10 - 30))
    
def IP_maquina():
    dic_interfaces = psutil.net_if_addrs()
    texto_ip = 'Informação do IP da máquina:'
    textip = font.render(texto_ip, 1, branco)
    tela.blit(textip, (20,  7*altura_tela/10 + 20))
    texto_ET = 'Ethernet: ' + str(dic_interfaces['Ethernet'][1].address)
    textet = font.render(texto_ET, 1, verde)
    tela.blit(textet, (20,  7*altura_tela/10 + 40))
    texto_CL1 = 'Conexão Local* 1: ' + str(dic_interfaces['Conexão Local* 1'][1].address)
    textcl1 = font.render(texto_CL1, 1, verde)
    tela.blit(textcl1, (20,  7*altura_tela/10 + 60))
    texto_CL2 = 'Conexão Local* 2: ' + str(dic_interfaces['Conexão Local* 2'][1].address)
    textcl2 = font.render(texto_CL2, 1, verde)
    tela.blit(textcl2, (20,  7*altura_tela/10 + 80))
    texto_WF = 'Wi-Fi: ' + str(dic_interfaces['Wi-Fi'][1].address)
    textwf = font.render(texto_WF, 1, verde)
    tela.blit(textwf, (20,  7*altura_tela/10 + 100))
    texto_PI = 'Loopback Pseudo-Interface 1: ' + str(dic_interfaces['Loopback Pseudo-Interface 1'][0].address)
    textpi = font.render(texto_PI, 1, verde)
    tela.blit(textpi, (20,  7*altura_tela/10 + 120))

  # Cria relógio
clock = pygame.time.Clock()
cont = 60

terminou = False
while not terminou:
      # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    # Fazer a atualização a cada segundo:
    if cont == 60:
        mostra_uso_memoria()
        mostra_uso_cpu()
        mostra_uso_disco()
        IP_maquina()
        cont = 0
    
      # Atualiza o desenho na tela
    pygame.display.update()
      # 60 frames por segundo
    clock.tick(60)
    cont += 1
  # Finaliza a janela
pygame.display.quit()