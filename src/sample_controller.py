import pygame
from player import Player

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    self.background = pygame.Surface((self.width, self.height))
    self.background.fill("lightblue")
    
    doodle = Player((self.width/2, self.height/2))
    
    pygame.display.flip()
    
  # def mainloop(self):
  #   #select state loop
    
  
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
