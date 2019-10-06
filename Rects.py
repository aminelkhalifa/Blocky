import pygame
WHITE = (255, 255, 255)


class Rects(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # State should be 'jumping' to prevent double jumping
        self.state = "standing"
        # Velocity turns to 100 when jumping then -9.8/s
        self.velocity = 0
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    #       JUMP
    # _ Check state and only execute if == "standing"
    # _ Use velocity (-10) to mimic arc of a jump
    def jump(self):
        if self.state == "standing":
            self.velocity = 100
            self.state = "jumping"
            self.jumpdate()

#TESTING
    def jumpdate(self):
        while self.velocity > -100:
            self.rect.y -= 1 * (self.velocity/100.0)
            self.velocity -= 10
            print (self.rect.y)


    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            sys.exit()
