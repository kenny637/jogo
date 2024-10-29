from typing import Any
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer_music.set_volume(0.9)
musica_de_fundo = pygame.mixer.music.load('Super Mario Bros. Theme Song.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Efeito sonoro da moeda do Mario..mp3')
barulho_colisao.set_volume(0.9)

largura = 640
altura = 500

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('RPG')
relogio = pygame.time.Clock()

class personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('download1.png'))
        self.sprites.append(pygame.image.load('download2.png'))
        self.sprites.append(pygame.image.load('download3.png'))
        self.sprites.append(pygame.image.load('download4.png'))
        self.sprites.append(pygame.image.load('download5.png'))
        self.sprites.append(pygame.image.load('download6.png'))
        self.sprites.append(pygame.image.load('download7.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*2, 128*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def pesonagem(self):
        self.animar = True
    def update(self):
        if self.animar == True:
            self.atual += 0.01
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*2, 128*2))

todas_as_sprites = pygame.sprite.Group()
personagem = personagem()
todas_as_sprites.add(personagem)
while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        todas_as_sprites.draw(tela)
        todas_as_sprites.update(      )
        pygame.display.flip()
    pygame.display.flip()