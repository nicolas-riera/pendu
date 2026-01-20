# Libraries

import pygame

from src.lib.menu import *

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Pendu")

    screen = pygame.display.set_mode((800,800))
    my_fonts = pygame.font.SysFont('Arial', 30), pygame.font.SysFont('Arial', 50)
    clock = pygame.time.Clock()

    menu(screen, clock, my_fonts)