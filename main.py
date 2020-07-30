import pygame
import os
img_path = os.path.join('Tet.png')


class character(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        character.image = pygame.image.load('Tet.png')
        self.image = character.image
        self.image = pygame.transform.scale(self.image,(600,600))

        self.x = 50
        self.y = 50
        self.hitbox = (self.x, self.y, 55, 55)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def movement(self):
        key = pygame.key.get_presssed()

        if key[pygame.K_DOWN]:
            self.y -= 1
        if key[pygame.K_UP]:
            self.y += 1
        if key[pygame.K_LEFT]:
            self.x -= 1
        if key[pygame.K_RIGHT]:
            self.x += 1


pygame.init()
screen_width = 600
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))

Tet = character()
clock = pygame.time.Clock

running = True
while running:
    for event in pygame.event.get():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

    screen.fill((255, 255, 255))
    Tet.draw(screen)

character.movement(Tet)

pygame.display.update()

clock.tick(60)
