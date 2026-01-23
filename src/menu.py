# Libraries

import os
import pygame

from src.pygame_events import *
from src.options import *
from src.game import *
from src.popup import *
from src.dark_mode import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Assets loading

logo_title = pygame.image.load(os.path.join(BASE_DIR, "../", "assets", "img", "logo_title.png"))

# Functions

def menu(screen, clock, my_fonts, is_dark_mode):

    error_popup_empty = False

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        is_dark_mode, text_color = is_dark_modes(screen, is_dark_mode)
        
        logo_title_rect = logo_title.get_rect(center=(650, 500))
        logo_title_scaled = pygame.transform.scale(logo_title, (logo_title.get_size()[0]*0.5, logo_title.get_size()[1]*0.5))
        screen.blit(logo_title_scaled, logo_title_rect)

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 450, 203, 80))
        play_button = pygame.Rect((295, 450, 203, 80))
        play_button_text = my_fonts[0].render("Jouer", True, text_color)
        screen.blit(play_button_text, (360, 470))

        pygame.draw.rect(screen, (168, 168, 168), (295, 560, 203, 80))
        option_button = pygame.Rect((295, 560, 203, 80))
        option_button_text = my_fonts[0].render("Options", True, text_color)
        screen.blit(option_button_text, (350, 580))  

        # Logic

        if escpressed:
            pygame.quit()
            raise SystemExit
        
        elif error_popup_empty:
            error_popup_empty = ok_popup(screen, clock, my_fonts, mouseclicked, "La liste est vide.", (213, 315))
            if not error_popup_empty:
                continue
        
        elif play_button.collidepoint(pygame.mouse.get_pos()) or option_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    if read_words() != []:
                        game(screen, clock, my_fonts, is_dark_mode)
                    else:
                        error_popup_empty = True
                else:
                    options(screen, clock, my_fonts, is_dark_mode)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)   
            