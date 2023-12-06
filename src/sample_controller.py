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

        self.doodle = Character((self.width/2), (self.height - 60))
        
        self.platform_group = pygame.sprite.Group()
        platform = Platforms(self.width // 2 - 50, self.height // 2 + 250, 100)
        self.platform_group.add(platform)
        
        self.gravity = 1
        self.max_plats = 10
        
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
            
            # plat_width = random.randint(40, 60)
            # plat_x = random.randint(0, self.width - plat_width)
            # plat_y = self.platform_group.sprites()[-1].rect.y - random.randint(80, 120)
            # platform = Platforms(plat_x, plat_y, plat_width)

            if len(self.platform_group) < self.max_plats:
                plat_width = random.randint(40, 60)
                plat_x = random.randint(0, self.width - plat_width)
                plat_y = self.platform_group.sprites()[-1].rect.y - random.randint(80, 120)
                platform = Platforms(plat_x, plat_y, plat_width)
                self.platform_group.add(platform)
            
            # for platform in self.platform_group:
            #     if platform.rect.colliderect(self.doodle.rect.x, self.doodle.rect.y, self.width, self.height):
            #         if self.doodle.rect.bottom < platform.rect.centery:
            #             if self.doodle.velocity_y > 0:
            #                 self.doodle.rect.bottom = platform.rect.top
            #                 dy = 0
            #                 self.doodle.velocity_y = -20
                
            for platform in self.platform_group:
                if platform.rect.colliderect(self.doodle.rect):
                    if self.doodle.rect.bottom <= platform.rect.top + 50:  
                        self.doodle.rect.bottom = platform.rect.top
                        self.doodle.velocity_y = -20
                         
            scroll = self.doodle.update_jump(self.gravity)
            self.doodle.wrap_around(self.width) 

            self.screen.blit(self.background, (0, 0))
            pygame.draw.line(self.screen, "white", (0, self.doodle.scroll_threshold), (self.width, self.doodle.scroll_threshold))
            
            self.platform_group.update(scroll)
            
            self.platform_group.draw(self.screen)
            self.screen.blit(self.doodle.image, self.doodle.rect.topleft)
            pygame.draw.rect(self.screen, "white", self.doodle.rect, 2)

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
