# Libraries

import os
import pygame

#from src.lib.words_mgt import *
# read_words()->list add_word(word:str) reset_list() remove_word(word_index) 
from src.lib.pygame_events import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Assets loading


# Functions

def options(screen, clock, my_fonts):

    while True:
        
        # pygame events

        mouseclicked, echappressed = pygame_events()

        # Rendering  

        screen.fill("white") 
        

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 450, 203, 80))
        words_button = pygame.Rect((295, 450, 203, 80))
        words_button_text = my_fonts[0].render("Mots", True, (0, 0, 0))
        screen.blit(words_button_text, (365, 470))

        pygame.draw.rect(screen, (168, 168, 168), (295, 560, 203, 80))
        return_button = pygame.Rect((295, 560, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 580))

        pygame.display.flip()  
        clock.tick(60)     

        # Logic

        if echappressed:
            break
        
        if words_button.collidepoint(pygame.mouse.get_pos()) or return_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if words_button.collidepoint(pygame.mouse.get_pos()):
                    print("words")
                    #words_menu(screen,clock,my_fonts)
                else:
                    print("return")
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 