# Libraries

import pygame
import os

from src.lib.menu import *
from src.lib.words_mgt import *

# Variables

FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "font", "LiberationSans-Regular.ttf")

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Pendu")

    pygame.key.set_repeat(400, 50)

    screen = pygame.display.set_mode((800,800))
    my_fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)
    clock = pygame.time.Clock()

    if read_words() == []:
        reset_words()

    menu(screen, clock, my_fonts)