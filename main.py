import pygame
import os
img_path = os.path.join('player.png')

class character(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    character.image = pygame.image.load('Tet.png')
    self.image = character.image
    #self.image = pygame.transform.scale(self.image(50,50))
   
    self.x = 50
    self.y = 50
    self.hitbox = (self.x,self.y, 55, 55)

  def draw(self, surface):
   surface.blit(self.image,(self.x,self.y))




pygame.init()
screen_width = 600
screen_hight = 600  
screen = pygame.display.set_mode((screen_width,screen_hight))

Sprite = character()
#clock = pygame.time.clock

running = True
while running:
  for event in pygame.event.get():
    
     if key[pygame.K_DOWN] and self.y < hight -50:
       if event.key == pygame.K_UP:
         y -= 50
       if event.key == pygame.K_DOWN:
         y += 50
       if event.key == pygame.K_RIGHT:
         x += 50
       if event.key == pygame.K_LEFT:
         x -= 50
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
     pygame.quit()
     running = False
 
  screen.fill((255,255,255))
  Sprite.draw(screen)

  pygame.display.update()

  #clock.tick(60)
