import pygame
from character import Character

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size(())
    self.background = pygame.Surface((self.width, self.height))
    self.background.fill("lightblue")
    
    self.doodles = pygame.sprite.Group()
    doodle = Character((self.width/2), (self.height/2))
    self.doodles.add(doodle)
        
    pygame.display.flip()
    
  def mainloop(self):
  #   #select state loop
      running = True
      clock = pygame.time.Clock()

      while running:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  running = False

          self.doodles.update()

          self.screen.blit(self.background, (0, 0))
          self.doodles.draw(self.screen)

          pygame.display.flip()
          clock.tick(60)

      pygame.quit()

    
  
  # ### below are some sample loop states ###

  # def menuloop(self):
    
  #     #event loop

  #     #update data

  #     #redraw
      
  # def gameloop(self):
  #     #event loop

  #     #update data

  #     #redraw
    
  # def gameoverloop(self):
  #     #event loop

  #     #update data

  #     #redraw
