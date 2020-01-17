import pygame

pygame.init()

window = pygame.display.set_mode((640,600))

pygame.mixer.music.load('sounds/free.mp3')

pygame.mixer.music.play(-1)