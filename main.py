# Libraries

import pygame
import os

from src.menu import *
from src.words_mgt import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "font", "LiberationSans-Regular.ttf")

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Pendu")
    pygame.display.set_icon(pygame.image.load(os.path.join(BASE_DIR, "assets", "img", "logo.png")))

    pygame.key.set_repeat(400, 50)

    screen = pygame.display.set_mode((800,800))
    my_fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)
    clock = pygame.time.Clock()

    check_empty_last_line()
    check_empty_last_line_config()

    if read_words() == []:
        reset_words()

    if read_config_file() == []:
        default_config()

    menu(screen, clock, my_fonts)