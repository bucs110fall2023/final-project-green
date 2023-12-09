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
        self.start_background = pygame.Surface((self.width, self.height))
        self.start_background.fill("cornflowerblue")
        self.background.fill("lightblue")
        pygame.display.set_caption("CS 110 Final Project - Monkey Jump")
        self.start_button = pygame.Rect(200, 400, 100, 50)
        self.restart_button = pygame.Rect(200, 450, 110, 50)

        self.doodle = Character((self.width/2), (self.height - 60))
        
        start_platform = Platforms(self.width // 2 - 50, self.height - 40, 100)
        
        self.platform_group = pygame.sprite.Group()
        platform = Platforms(self.width // 2 - 50, self.height // 2 + 250, 100)
        self.platform_group.add(platform)
        self.platform_group.add(start_platform)
        
        self.GRAVITY = 1
        self.MAX_PLATS = 10
        
        self.font = pygame.font.SysFont("Arial", 55)
        
        self.clock = pygame.time.Clock()
        self.FPS = 60

        pygame.display.flip()

    def mainloop(self):
        running = True
        move_left = False
        move_right = False
        game_over = False
        start_screen = True

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
            
            if start_screen == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(pygame.mouse.get_pos()):
                        start_screen = False
                self.screen.blit(self.start_background, (0, 0))
                
                pygame.draw.rect(self.screen, "ivory", self.start_button)
                font = pygame.font.Font(None, 36)
                text = font.render("START", True, "black")
                self.screen.blit(text, (self.width/2 - 40, self.height/2 - 13))
                
                pygame.display.flip()            
            else:
                if game_over == False:
                    if len(self.platform_group) < self.MAX_PLATS:
                        plat_width = random.randint(40, 60)
                        plat_x = random.randint(0, self.width - plat_width)
                        plat_y = self.platform_group.sprites()[-1].rect.y - random.randint(80, 120)
                        platform = Platforms(plat_x, plat_y, plat_width)
                        self.platform_group.add(platform)
                        
                    for platform in self.platform_group:
                        if self.doodle.velocity_y > 0:
                            if platform.rect.colliderect(self.doodle.rect):
                                if self.doodle.rect.bottom <= platform.rect.top + 50:  
                                    self.doodle.rect.bottom = platform.rect.top
                                    self.doodle.velocity_y = -20
                                
                    scroll = self.doodle.update_jump(self.GRAVITY)
                    self.doodle.wrap_around(self.width) 

                    self.screen.blit(self.background, (0, 0))
                    
                    self.platform_group.update(scroll)
                    
                    self.platform_group.draw(self.screen)
                    self.screen.blit(self.doodle.image, self.doodle.rect.topleft)
                    
                    if self.doodle.rect.top > self.height:
                        game_over = True

                    pygame.display.flip()
                    
                    self.clock.tick(self.FPS)
                else:
                    game_over_text = self.font.render("Game Over!", True, "dimgray")
                    self.screen.blit(game_over_text, (100, 400))
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.restart_button.collidepoint(pygame.mouse.get_pos()):
                            start_screen = True
                            game_over = False
                            self.__init__()
                        self.screen.blit(self.start_background, (0, 0))
                
                    pygame.draw.rect(self.screen, "ivory", self.restart_button)
                    font = pygame.font.Font(None, 36)
                    text = font.render("RESTART", True, "black")
                    self.screen.blit(text, (self.width/2 - 50, self.height/2 + 37))
                    
                    pygame.display.flip()

        pygame.quit()