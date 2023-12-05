import pygame
import random
from character import Character
from platforms import Platforms

class Controller:
  
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 850))
        self.width, self.height = pygame.display.get_window_size()
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill("lightblue")

        self.doodles = pygame.sprite.Group()
        self.doodle = Character((self.width/2), (self.height - 60))
        self.doodles.add(self.doodle)
        
        self.platforms = pygame.sprite.Group()
        platform = Platforms(self.width // 2 - 50, self.height // 2 + 250, 100)
        self.platforms.add(platform)
        
        self.gravity = 1
        self.jump_velocity = -20
        
        self.clock = pygame.time.Clock()
        self.fps = 60

        pygame.display.flip()

    def mainloop(self):
        #select state loop
        running = True
        move_left = False
        move_right = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        move_left = True
                    elif event.key == pygame.K_d:
                        move_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        move_left = False
                    elif event.key == pygame.K_d:
                        move_right = False              
                
            if(move_left):
                self.doodle.rect.x -= 10
            elif(move_right):
                self.doodle.rect.x += 10
                
            p_w = random.randint(40, 60)
            p_x = random.randint(0, 500 - p_w)
            p_y = self.platforms.sprites()[-1].rect.y - random.randint(80, 120)
            platform = Platforms(p_x, p_y, p_w)

            if len(self.platforms) < 10:
                self.platforms.add(platform)

            self.doodle.update_jump(self.gravity)
            self.doodle.wrap_around(self.width)
            
            self.doodles.update()

            self.screen.blit(self.background, (0, 0))
            self.doodles.draw(self.screen)
            self.platforms.draw(self.screen)

            pygame.display.flip()
            
            self.clock.tick(self.fps)

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
