# Libraries

import os
import pygame
import math

from src.pygame_events import *
from src.popup import *
from src.scores_mgt import *
from src.render_adaptive_text import *
from src.dark_mode import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "../", "assets", "font", "LiberationSans-Regular.ttf")

# Assets loading

ESC_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "esc_sfx.mp3"))
MENU_BUTTON_CLICK_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "menu_button_click_sfx.wav"))

# Functions

def scores(screen, clock, my_fonts, is_dark_mode):

    '''
    Pygame scores menu loop.
    ### PARAMETERS
            screen: pygame.Surface
            clock: pygame.Clock
            my_fonts: tuple[pygame.Font, pygame.Font]
            is_dark_mode: bool
    '''

    check_empty_last_line_scores()
    scores_list_current_page = 0

    while True:
        
        scores_list = read_scores()
        scores_list.sort(key=lambda x: x[2])
        scores_list_pages = math.ceil(len(scores_list) / 10)

        previous_page_rect = None
        next_page_rect = None
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        name_section_text = my_fonts[0].render("JOUEUR", True, text_color)
        screen.blit(name_section_text, (60, 50))
        word_section_text = my_fonts[0].render("MOT", True, text_color)
        screen.blit(word_section_text, (300, 50))
        error_section_text = my_fonts[0].render("ERREURS", True, text_color)
        screen.blit(error_section_text, (600, 50))

        pygame.draw.line(screen, text_color, (50, 90), (750, 90), 2)

        for i in range (scores_list_current_page*10, len(scores_list)):
            if (i-scores_list_current_page * 10) < 10:
                y_offset = 50*(i-scores_list_current_page*10)
                pygame.draw.line(screen, text_color, (50, 92 + y_offset), (750, 92 + y_offset), 2)
                render_adaptive_text(
                            screen=screen,
                            text=str(scores_list[i][0].capitalize()),
                            x=60,
                            y=100 + y_offset,
                            max_width=200,
                            font_path=FONT_PATH,
                            color=text_color
                        )
                render_adaptive_text(
                            screen=screen,
                            text=str(scores_list[i][1].capitalize()),
                            x=300,
                            y=100 + y_offset,
                            max_width=200,
                            font_path=FONT_PATH,
                            color=text_color
                        )
                render_adaptive_text(
                            screen=screen,
                            text=str(scores_list[i][2]),
                            x=600,
                            y=100 + y_offset,
                            max_width=200,
                            font_path=FONT_PATH,
                            color=text_color
                        )

        if scores_list_pages > 1:

            if scores_list_current_page != 0:
                previous_page_arrow = my_fonts[1].render("<", True, text_color)
                previous_page_rect = previous_page_arrow.get_rect(topleft=(70, 660))
                screen.blit(previous_page_arrow, (70, 660))
            else:
                previous_page_rect = None

            if scores_list_current_page != scores_list_pages-1:
                next_page_arrow = my_fonts[1].render(">", True, text_color)
                next_page_rect = next_page_arrow.get_rect(topleft=(700, 660))
                screen.blit(next_page_arrow, (700, 660))
            else:
                next_page_rect = None


        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (168, 168, 168), (295, 650, 203, 80))
        return_button = pygame.Rect((295, 650, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 670)) 

        page_indicator_text = my_fonts[0].render(f"Page {scores_list_current_page + 1}", True, text_color)
        screen.blit(page_indicator_text, (352, 743))

        # Logic

        hover = False

        if next_page_rect is not None:
            if next_page_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                    scores_list_current_page += 1
                else:
                    hover = True   
        
        if previous_page_rect is not None:
            if previous_page_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                    scores_list_current_page -= 1
                else:
                    hover = True

        if escpressed:
            pygame.mixer.Sound.play(ESC_SFX)
            break
        
        elif return_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                break
            else:
                hover = True

        else:
            hover = False

        if hover == True:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)   
            