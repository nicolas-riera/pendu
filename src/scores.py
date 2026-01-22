# Libraries

import os
import pygame
import math

from src.pygame_events import *
from src.popup import *
from src.scores_mgt import *
from src.render_adaptive_text import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Functions

def scores(screen, clock, my_fonts):

    check_empty_last_line_scores()
    
    while True:
        
        # read_scores() -> [(username, score, errors)]
        scores_list = read_scores()
        scores_list_current_page = 0
        scores_list_pages = math.ceil(len(scores_list) / 30)

        previous_page_rect = None
        next_page_rect = None
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen.fill("white") 
        
        for i in range (scores_list_current_page*20, len(scores_list)):
            render_adaptive_text(
                        screen=screen,
                        text=scores_list[i][0].capitalize(),
                        x=50,
                        y=100 + 50 * (i-scores_list_current_page * 20),
                        max_width=200,
                        font_path=FONT_PATH
                    )
            render_adaptive_text(
                        screen=screen,
                        text=scores_list[i][1],
                        x=250,
                        y=100 + 50 * (i-scores_list_current_page * 20),
                        max_width=200,
                        font_path=FONT_PATH
                    )
            render_adaptive_text(
                        screen=screen,
                        text=scores_list[i][2],
                        x=500,
                        y=100 + 50 * (i-scores_list_current_page * 20),
                        max_width=200,
                        font_path=FONT_PATH
                    )
            
        if scores_list_pages > 1:

            if scores_list_current_page != 0:
                previous_page_arrow = my_fonts[1].render("<", True, (0, 0, 0))
                previous_page_rect = previous_page_arrow.get_rect(topleft=(70, 660))
                screen.blit(previous_page_arrow, (70, 660))
            else:
                previous_page_rect = None

            if scores_list_current_page != scores_list_pages-1:
                next_page_arrow = my_fonts[1].render(">", True, (0, 0, 0))
                next_page_rect = next_page_arrow.get_rect(topleft=(700, 660))
                screen.blit(next_page_arrow, (700, 660))
            else:
                next_page_rect = None


        # Draw.rect(surface, color, (x position, y position, x width, y width))

        pygame.draw.rect(screen, (168, 168, 168), (295, 600, 203, 80))
        return_button = pygame.Rect((295, 600, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 620)) 

        page_indicator_text = my_fonts[0].render(f"Page {scores_list_current_page + 1}", True, (0, 0, 0))
        screen.blit(page_indicator_text, (352, 743))

        # Logic

        hover = False

        if next_page_rect is not None:
            if next_page_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                    words_list_current_page += 1
                else:
                    hover = True   
        
        if previous_page_rect is not None:
            if previous_page_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                    words_list_current_page -= 1
                else:
                    hover = True

        if escpressed:
            break
        
        elif return_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

        if hover == True:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)   
            