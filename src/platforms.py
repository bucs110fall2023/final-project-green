import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, img = "assets/wood.png"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        
        self.image = pygame.transform.scale(self.image, (width, 10))
        
    def update(self, scroll):
        self.rect.y += scroll
        if self.rect.top > self.height:
            self.kill()