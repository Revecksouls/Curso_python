
import pygame
from pygame.locals import *
from sys import exit
from random import * 

pygame.init()

#criando a janela
altura = 480
largura = 640
tela = pygame.display.set_mode((largura,altura))

# definindo posição e tamanho do objeto
pos_x = altura / 2 
pos_y = largura / 2
largura_retangulo = 30
altura_retangulo = 35

#denfinindo posicao e tamanho do circulo
pos_y_circulo = 40
pos_x_circulo = 40
raio_circulo = 10

#definindo fonte 
fonte = pygame.font.SysFont("arial",20 ,True , False)
pontos = 0 

# definir o titulo
pygame.display.set_caption("Jogo Senai")
#modificar a taxa de atualizacao de pixels/segundos
relogio = pygame.time.Clock()
while True:
    relogio.tick(90)
    tela.fill((0,0,0))
    mensagem = f"ponto: {pontos}"
    textoformatado = fonte.render(mensagem , True ,(255,255,255))
    #colocando os eventos no pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
           
        # if event.type == KEYDOWN:
        #     if event.key == K_w:
        #         pos_y -= 10  
        #     if event.key == K_s:
        #         pos_y += 10
        #     if event.key == K_d:
        #         pos_x += 10
        #     if event.key == K_a:
        #         pos_x -= 10 
    #clicar somente uma vez para mover         
    if pygame.key.get_pressed()[K_w]: 
        pos_y -= 5
    elif pygame.key.get_pressed()[K_s]:
        pos_y += 5 
    elif pygame.key.get_pressed()[K_a]:
        pos_x -= 5 
    elif pygame.key.get_pressed()[K_d]:
        pos_x += 5 
    
    retangulo = pygame.draw.rect(tela,(255,255,255),(pos_x,pos_y,largura_retangulo,altura_retangulo))
    
    circulo = pygame.draw.circle(tela, (255,255,255),(pos_x_circulo,pos_y_circulo), raio_circulo)
    
    if retangulo.colliderect(circulo):
        pos_x_circulo = randint(40,600)
        pos_y_circulo = randint(50,430)
        pontos += 1
    tela.blit(textoformatado,(400,40))
    #atualizar o jogo a cada interaçao
    pygame.display.update()

