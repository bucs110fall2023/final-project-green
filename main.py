import pygame
import sys 
sys.path.append("src")

from src.sample_controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()