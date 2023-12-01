import pygame
from character import Character

class Controller:
  
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 850))
        self.width, self.height = pygame.display.get_window_size()
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill("lightblue")

        self.doodles = pygame.sprite.Group()
        self.doodle = Character((self.width/2), (self.height/2))
        self.doodles.add(self.doodle)
        
        self.gravity = 2
        
        self.clock = pygame.time.Clock()
        self.fps = 60

        pygame.display.flip()

    def mainloop(self):
        #select state loop
        running = True
        move_left = False
        move_right = False
        move_jump = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        move_left = True
                    elif event.key == pygame.K_d:
                        move_right = True
                    elif event.key == pygame.K_SPACE:
                        self.doodle.rect.y -= 100
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        move_left = False
                    elif event.key == pygame.K_d:
                        move_right = False              
                
            if(move_left):
                self.doodle.rect.x -= 5
            elif(move_right):
                self.doodle.rect.x += 5
            
            if self.doodle.rect.y < self.height - self.doodle.rect.height:
                self.doodle.rect.y += self.gravity   
            
            self.doodles.update()

            self.screen.blit(self.background, (0, 0))
            self.doodles.draw(self.screen)

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
