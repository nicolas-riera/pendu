# Libraries

import os
import pygame

from src.lib.pygame_events import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Assets loading

logo_title = pygame.image.load(os.path.join(BASE_DIR, "../" ,"img", "logo_title.png"))

# Functions

def menu(screen, clock, my_fonts):

    while True:
        
        # pygame events

        mouseclicked, echappressed = pygame_events()

        # Rendering  

        screen.fill("white") 
        
        logo_title_rect = logo_title.get_rect(center=(650, 500))
        logo_title_scaled = pygame.transform.scale(logo_title, (logo_title.get_size()[0]*0.5, logo_title.get_size()[1]*0.5))
        screen.blit(logo_title_scaled, logo_title_rect)

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 450, 203, 80))
        play_button = pygame.Rect((295, 450, 203, 80))
        play_button_text = my_fonts[0].render("Jouer", True, (0, 0, 0))
        screen.blit(play_button_text, (365, 470))

        pygame.draw.rect(screen, (168, 168, 168), (295, 560, 203, 80))
        option_button = pygame.Rect((295, 560, 203, 80))
        option_button_text = my_fonts[0].render("Options", True, (0, 0, 0))
        screen.blit(option_button_text, (356, 580))

        pygame.display.flip()  
        clock.tick(60)     

        # Logic

        if echappressed:
            pygame.quit()
            raise SystemExit
        
        if play_button.collidepoint(pygame.mouse.get_pos()) or option_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    print("game")
                    # tbd game
                else:
                    print("option")
                    # tbd option
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            