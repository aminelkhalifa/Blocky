import pygame
from Rects import Rects
pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

carryOn = True
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
player = Rects(RED, 30, 30)
player.rect.x = 200
player.rect.y = 300

goal = Rects(BLUE, 30, 30)
goal.rect.x = 600
goal.rect.y = 300

all_sprites_list.add(player, goal)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn = False


    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        player.moveRight(5)
    if keys[pygame.K_SPACE]:
        player.jump()

    #Game Logic
    all_sprites_list.update()
    player.checkCollision(player, goal)

    #Drawing on Screen
    screen.fill(BLACK)

    #Draws all the sprites in sprite list
    all_sprites_list.draw(screen)

    # Updates screen
    pygame.display.flip()

    clock.tick(60)
