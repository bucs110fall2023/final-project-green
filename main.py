import pygame
import sys 
sys.path.append("src")

from src.sample_controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()