import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "assets/monkey.png"):
        """
        Initializes the character sprite

        Args:
            x (int): starting x-coordinate for the sprite of the character
            y (int): starting y-coordinate of the sprite of the character
            img (str): path to the image file for the sprite of the character
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.WIDTH = 30
        self.HEIGHT = 45
        self.rect = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        self.rect.x = x 
        self.rect.y = y
        self.rect.center = (x, y)
        self.velocity_y = 0
        self.SCROLL_THRESHOLD = 200
        self.scroll = 0

        pygame.display.flip()
        
    def update_jump(self, gravity):
        """
        Updates position of the sprite based on how the sprite jumps 

        Args:
            gravity (float): applies gravity to the sprite

        Returns:
            float: the scroll value that is used to scroll the screen 
        """
        self.scroll = 0 
        self.dx = 0
        self.dy = 0
        
        self.w, self.h = pygame.display.get_window_size()
        
        self.velocity_y += gravity
        self.dy += self.velocity_y
        
        if self.rect.top <= self.SCROLL_THRESHOLD:
            if self.velocity_y < 0:
                self.scroll = -self.dy  
        
        self.rect.x += self.dx
        self.rect.y += self.dy + self.scroll
        
        return self.scroll
        
    def wrap_around(self, screen_width):
        """
        Lets the sprite reenter the other side of the screen of the sprite leaves the opposite side

        Args:
            screen_width (int): value representing the width of the screen
        """
        if self.rect.x > screen_width:
            self.rect.x = -self.rect.width
        elif self.rect.x < -self.rect.width:
            self.rect.x = screen_width