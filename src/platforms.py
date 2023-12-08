import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, img = "assets/rectangle.png"):
        """
        Initializes the platform sprite 

        Args:
            x (int): starting x-coordinate for the sprite of the platform
            y (int): starting y-coordinate for the sprite of the platform 
            width (int): represents the width of the platform 
            img (str): path to the image for the sprite of the platform
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        
    def update(self, scroll):
        """
        Updates the position of the platform based on the scrolling of the screen

        Args:
            scroll (int): the value of the scrolling of the screen
        """
        self.rect.y += scroll
        self.w, self.h = pygame.display.get_window_size()
        if self.rect.top > self.h:
            self.kill()