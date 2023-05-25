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

cloud = pygame.image.load("image/cloud.png").convert_alpha()
cloud_x = 842
cloud_y = 50


ghost = pygame.image.load("image/ghost.png").convert_alpha()
ghost_list_in_game = []

proigrysh = pygame.image.load("image/proigysh.png")

player_anim = 0
bg_x = 0
player_speed = 10
player_x = 100
player_y = 415
is_jump = False
jump_count = 12
bullet = pygame.image.load("image/bullet.png").convert_alpha()
bullets = []
bullets_num = 8


# таймер для спавна призрака
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)


mp3 = pygame.mixer.Sound("mp3/pawapepe_gemabody_Павапепе_гемабоди_х_За.mp3")
mp3.play()

game_play = True

running = True