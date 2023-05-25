#Адам
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
#Адам



#Имам
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
#Создал переменную для цикла рахьмана
running = True
#Имам

#Рахман
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))
    screen.blit(cloud, (cloud_x, cloud_y))

    if game_play:

    # воображаемые квадраты
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    # спам призраков
        if ghost_list_in_game:
            for (i, element) in enumerate(ghost_list_in_game):
                screen.blit(ghost, element)
                element.x -= 15

                if element.x < -15:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(element):
                     game_play = False

        keys = pygame.key.get_pressed()

    # снаряд
        if bullets:
            for(i, element) in enumerate(bullets):
                screen.blit(bullet, (element.x, element.y))
                element.x += 25

                if element.x > 850:
                    bullets.pop(i)

                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if element.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim], (player_x, player_y))
     #Рахман

     #Алихан
     # отслеживание нажатий кнопок, движение влево вправо

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
            bg_x += 10
            cloud_x += 10
        elif keys[pygame.K_RIGHT] and player_x < 740:
            player_x += player_speed
            bg_x -= 10
            cloud_x -= 10
        else:
            bg_x -= 5
            cloud_x -= 1

    # анимация прыжка
        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -12:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 3
            else:
                is_jump = False
                jump_count = 12
        #Алихан
        #Zelim
        # анимация персонажа
        if player_anim == 3:
            player_anim = 0
        else:
            player_anim += 1

    else:
            screen.blit(proigrysh, (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(842, 415)))
            #___
        if game_play and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_num > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y + 10)))
            bullets_num -= 1
    pygame.display.update()

    clock.tick(12)
    #Zelim