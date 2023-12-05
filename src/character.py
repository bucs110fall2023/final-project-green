import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "assets/doodle.jpg"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.velocity_y = 0
        self.is_jumping = False
        
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        pygame.display.flip()
        
    def update_jump(self, gravity):
        self.rect.y += self.velocity_y
        self.velocity_y += gravity

        if self.rect.y >= 850 - self.rect.height:
            self.velocity_y = -20 
            self.rect.y = 850 - self.rect.height
            
    def wrap_around(self, screen_width):
        if self.rect.x > screen_width:
            self.rect.x = -self.rect.width
        elif self.rect.x < -self.rect.width:
            self.rect.x = screen_width