import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musica_fundo = pygame.mixer.music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')


largura = 600
altura = 480

x = largura//2
y = altura//2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0

fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Ai balde')

relogio = pygame.time.Clock()

while True:

    relogio.tick(60)

    tela.fill((0,0,0))

    mensagem = f'Pontos: {pontos}'

    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_s:
                y = y + 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
        '''

    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    ret_verde = pygame.draw.rect(tela, (0,255,0), (x_azul, y_azul, 40, 50))
    
    if ret_vermelho.colliderect(ret_verde):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    if y >= altura:
        y = 0

    if x >= largura:
        x = 0

    tela.blit(texto_formatado, (200, 40))

    pygame.display.update()

