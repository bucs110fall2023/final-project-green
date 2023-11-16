import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "/Users/erichom/github-classroom/bucs110fall2023/final-project-green/assets/doodle.jpg"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y