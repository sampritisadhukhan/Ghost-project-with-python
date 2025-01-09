import pygame
pygame.init()
from time import sleep
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load("ratsasan.mp3")
pygame.mixer.music.play()
pygame.mixer.music.load("scary.mp3")
pygame.mixer.music.play()
sleep(3)
image = pygame.image.load("scr.jpg")
window.blit(image, (0,0))
pygame.display.update()
sleep(4)
