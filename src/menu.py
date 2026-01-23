# Libraries

import os
import pygame

from src.pygame_events import *
from src.options import *
from src.game import *
from src.popup import *
from src.scores_mgt import *
from src.scores import *
from src.dark_mode import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Assets loading

logo_title = pygame.image.load(os.path.join(BASE_DIR, "../", "assets", "img", "logo_title.png"))

# Functions

def menu(screen, clock, my_fonts):

    error_popup_empty = False
    is_dark_mode = True
    notice_username_input_popup = False
    notice_username_input_empty_popup = False

    usr_word = ""

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        text_color = light_dark_mode(screen, is_dark_mode)
        
        logo_title_rect = logo_title.get_rect(center=(650, 500))
        logo_title_scaled = pygame.transform.scale(logo_title, (logo_title.get_size()[0]*0.5, logo_title.get_size()[1]*0.5))
        screen.blit(logo_title_scaled, logo_title_rect)

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 400, 203, 80))
        play_button = pygame.Rect((295, 400, 203, 80))
        play_button_text = my_fonts[0].render("Jouer", True, (0, 0, 0))
        screen.blit(play_button_text, (360, 420))

        pygame.draw.rect(screen, (236, 179, 50), (295, 500, 203, 80))
        scores_button = pygame.Rect((295, 500, 203, 80))
        scores_button_text = my_fonts[0].render("Scores", True, (0, 0, 0))
        screen.blit(scores_button_text, (351, 520))

        pygame.draw.rect(screen, (168, 168, 168), (295, 600, 203, 80))
        option_button = pygame.Rect((295, 600, 203, 80))
        option_button_text = my_fonts[0].render("Options", True, (0, 0, 0))
        screen.blit(option_button_text, (346, 620))  

        # Logic

        if escpressed:
            pygame.quit()
            raise SystemExit
        
        elif error_popup_empty:
            error_popup_empty = ok_popup(screen, my_fonts, mouseclicked, "La liste est vide.", (213, 315))
            if not error_popup_empty:
                continue

        elif notice_username_input_popup:

            usr_input = keyboard_input(events)

            if usr_input == "backspace":
                usr_word = usr_word[:-1]
            elif usr_input == "enter":
                if usr_word != "":
                    notice_username_input_popup = False
                    change_username(usr_word)
                    game(screen, clock, my_fonts, is_dark_mode)

                    usr_word = ""
                    continue
                else:
                    notice_username_input_empty_popup = True
            elif len(usr_word) < 26:
                usr_word += usr_input
            
            notice_username_input_popup = username_input_popup(screen, my_fonts, mouseclicked, usr_word)

            if notice_username_input_empty_popup:
                notice_username_input_empty_popup = ok_popup(screen, my_fonts, mouseclicked, "Nom vide.", (287, 315))

            if not notice_username_input_popup:
                if usr_word != "":
                    change_username(usr_word)
                    game(screen, clock, my_fonts, is_dark_mode)

                    usr_word = ""
                    continue
                else:
                    notice_username_input_popup = True
                    notice_username_input_empty_popup = True

        elif play_button.collidepoint(pygame.mouse.get_pos()) or scores_button.collidepoint(pygame.mouse.get_pos()) or option_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    if read_words() != []:
                        if read_username() != "anonyme":
                            game(screen, clock, my_fonts, is_dark_mode)
                        else:
                            notice_username_input_popup = True
                    else:
                        error_popup_empty = True
                elif scores_button.collidepoint(pygame.mouse.get_pos()):
                    scores(screen, clock, my_fonts, is_dark_mode)
                else:
                    options(screen, clock, my_fonts, is_dark_mode)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)   
            