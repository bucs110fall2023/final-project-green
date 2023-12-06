import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, img = "assets/rectangle.png"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        
    def update(self, scroll):
        self.rect.y += scroll
        self.w, self.h = pygame.display.get_window_size()
        if self.rect.top > self.h:
            self.kill()