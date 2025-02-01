import pygame
from pygame import mixer

pygame.init()
mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('game')

icon = pygame.image.load('images/color.jpeg')
pygame.display.set_icon(icon)

plays = pygame.image.load('images/gema.jpg')

wal_left = [
    pygame.image.load('images/opt-removebg-preview.png'),
    pygame.image.load('images/opt-removebg-preview (1).png'),
    pygame.image.load('images/opt-removebg-preview (2).png'),
    pygame.image.load('images/opt-removebg-preview (3).png'),
    pygame.image.load('images/opt-removebg-preview (4).png'),
    pygame.image.load('images/opt-removebg-preview (5).png'),
    pygame.image.load('images/opt-removebg-preview (6).png'),
    pygame.image.load('images/opt-removebg-preview (7).png'),
    pygame.image.load('images/opt-removebg-preview (8).png'),
    pygame.image.load('images/opt-removebg-preview (9).png'),
    pygame.image.load('images/opt-removebg-preview (10).png'),
    pygame.image.load('images/opt-removebg-preview (11).png'),
]

wal_right = wal_left

player_anim = 1
player_speed = 9
player_x = 100
player_y = 300
ground_y = player_y  # Координата земли
is_jump = False
jump_count = 10
running = True

cloo = mixer.Sound('images/f0cfb0928390cfe.mp3')
cloo.play(-1)

while running:
    screen.blit(plays, (0, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 20:
        player_x -= player_speed
        screen.blit(wal_left[player_anim], (player_x, player_y))
    elif keys[pygame.K_RIGHT] and player_x < 800 - 50:
        player_x += player_speed
        screen.blit(wal_right[player_anim], (player_x, player_y))
    else:
        screen.blit(wal_right[player_anim], (player_x, player_y))

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1 if jump_count > 0 else -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
            player_y = ground_y  # Возвращаем игрока на землю

    if player_anim == len(wal_left) - 1:
        player_anim = 0
    else:
        player_anim += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                running = False
                pygame.quit()

    clock.tick(10)
