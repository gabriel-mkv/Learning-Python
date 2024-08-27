from emoji import emojize
import pygame
from time import sleep
pygame.init()
pygame.mixer_music.load('ex046.mp3')
print('\t\t' + ' DESAFIO 046 '.center(40, '=') + '\n')
print('\033[4;32mINICIANDO CONTAGEM PARA O ANO NOVO!\033[m'.center(66) + '\n')

for c in range(10, -1, -1):
    print(f'« {c:2d} »'.center(54))
    sleep(1)

print('\n' + emojize('É ANO NOVO!!!! :fireworks: :sparkler: :fireworks: :sparkler:').center(53))
pygame.mixer_music.play()
input(pygame.event.wait())
