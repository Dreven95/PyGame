import pygame
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((840, 533))
pygame.display.set_caption("и мам и пап")
icon = pygame.image.load("image/icon.png").convert_alpha()
pygame.display.set_icon(icon)
bg = pygame.image.load("image/fon.jpg").convert()
player = pygame.image.load("image/pers_left/pers_left1.png").convert_alpha()

walk_right = [
    pygame.image.load("image/pers_right/pers_right1.png").convert_alpha(),
    pygame.image.load("image/pers_right/pers_right2.png").convert_alpha(),
    pygame.image.load("image/pers_right/pers_right3.png").convert_alpha(),
    pygame.image.load("image/pers_right/pers_right4.png").convert_alpha(),
]
walk_left = [
    pygame.image.load("image/pers_left/pers_left1.png").convert_alpha(),
    pygame.image.load("image/pers_left/pers_left2.png").convert_alpha(),
    pygame.image.load("image/pers_left/pers_left3.png").convert_alpha(),
    pygame.image.load("image/pers_left/pers_left4.png").convert_alpha(),
]