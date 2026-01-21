# Libraries

import os
import pygame

from src.lib.words_mgt import *
from src.lib.pygame_events import *
from src.lib.keyboard_input import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Assets loading


# Functions

def options(screen, clock, my_fonts):

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen.fill("white") 

        settings_title_button_text = my_fonts[1].render("Options", True, (0, 0, 0))
        screen.blit(settings_title_button_text, (310, 120))

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 300, 203, 80))
        words_button = pygame.Rect((295, 300, 203, 80))
        words_button_text = my_fonts[0].render("Mots", True, (0, 0, 0))
        screen.blit(words_button_text, (365, 320))

        pygame.draw.rect(screen, (168, 168, 168), (295, 560, 203, 80))
        return_button = pygame.Rect((295, 560, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 580))

        pygame.display.flip()  
        clock.tick(60)     

        # Logic

        if escpressed:
            break
        
        if words_button.collidepoint(pygame.mouse.get_pos()) or return_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if words_button.collidepoint(pygame.mouse.get_pos()):
                    words_menu(screen,clock,my_fonts)
                elif return_button.collidepoint(pygame.mouse.get_pos()):
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

def words_menu(screen, clock, my_fonts):

    reset_popup = False
    
    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen.fill("white") 

        words_title_button_text = my_fonts[1].render("Mots", True, (0, 0, 0))
        screen.blit(words_title_button_text, (340, 120))

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 300, 203, 80))
        add_word_button = pygame.Rect((295, 300, 203, 80))
        add_word_button_text = my_fonts[0].render("Ajouter mot", True, (0, 0, 0))
        screen.blit(add_word_button_text, (322, 320))
        
        pygame.draw.rect(screen, (236, 179, 151), (295, 400, 203, 80))
        remove_word_button = pygame.Rect((295, 400, 203, 80))
        remove_word_button_text = my_fonts[0].render("Retirer mot", True, (0, 0, 0))
        screen.blit(remove_word_button_text, (322, 420))

        pygame.draw.rect(screen, (236, 179, 201), (295, 500, 203, 80))
        reset_word_button = pygame.Rect((295, 500, 203, 80))
        reset_word_button_text = my_fonts[0].render("Restaurer liste", True, (0, 0, 0))
        screen.blit(reset_word_button_text, (300, 520))

        pygame.draw.rect(screen, (168, 168, 168), (295, 600, 203, 80))
        return_button = pygame.Rect((295, 600, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 620))    

        # Logic

        if escpressed:
            break

        if reset_popup:
            reset_popup = popup(screen, clock, my_fonts, mouseclicked, "La liste a été restaurée.", (150, 315))

        else:
            if add_word_button.collidepoint(pygame.mouse.get_pos()) or return_button.collidepoint(pygame.mouse.get_pos()) or add_word_button.collidepoint(pygame.mouse.get_pos()) or remove_word_button.collidepoint(pygame.mouse.get_pos()) or reset_word_button.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if add_word_button.collidepoint(pygame.mouse.get_pos()):
                        add_word_menu(screen, clock, my_fonts)
                    elif return_button.collidepoint(pygame.mouse.get_pos()):
                        break
                    elif remove_word_button.collidepoint(pygame.mouse.get_pos()):
                        pass
                        #remove_words_menu(screen, clock, my_fonts)
                    elif reset_word_button.collidepoint(pygame.mouse.get_pos()):
                        reset_words()
                        reset_popup = True

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)       

        pygame.display.flip()  
        clock.tick(60) 

def add_word_menu(screen, clock, my_fonts):

    usr_word = ""
    error_found_popup = False
    error_too_short_popup = False

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Keyboard input logic

        usr_input = keyboard_input(events)

        if usr_input == "backspace":
            usr_word = usr_word[:-1]
        elif usr_input == "enter":
            if usr_word in read_words():
                error_found_popup = True
            elif len(usr_word) < 3:
                error_too_short_popup = True
            elif usr_word != "":
                break
        else:
            if len(usr_word) < 26:
                usr_word += usr_input

        # Rendering  

        screen.fill("white") 

        words_title_button_text = my_fonts[1].render("Ajouter un mot", True, (0, 0, 0))
        screen.blit(words_title_button_text, (230, 120))

        pygame.draw.rect(screen, (240, 240, 240), (70, 310, 660, 60))
        usr_word_display = my_fonts[0].render(usr_word, True, (0, 0, 0))
        screen.blit(usr_word_display, (75, 320))

        if usr_word == "":
            add_word_button_color = (224, 222, 218)
        else:
            add_word_button_color = (236, 179, 101)

        pygame.draw.rect(screen, add_word_button_color, (295, 500, 203, 80))
        add_word_button = pygame.Rect((295, 500, 203, 80))
        add_word_button_text = my_fonts[0].render("Ajouter mot", True, (0, 0, 0))
        screen.blit(add_word_button_text, (322, 520))

        pygame.draw.rect(screen, (168, 168, 168), (295, 600, 203, 80))
        return_button = pygame.Rect((295, 600, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 620))
        
        # Logic

        if error_found_popup:
            error_found_popup = popup(screen, clock, my_fonts, mouseclicked, "Le mot existe déjà.", (193, 315))
        elif error_too_short_popup:
            error_too_short_popup= popup(screen, clock, my_fonts, mouseclicked, "Le mot est trop court.", (168, 315))

        elif add_word_button.collidepoint(pygame.mouse.get_pos()) and not(return_button.collidepoint(pygame.mouse.get_pos())):
            if usr_word != "":
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                if mouseclicked:
                    if usr_word in read_words():
                        error_found_popup = True
                    elif len(usr_word) < 3:
                        error_too_short_popup = True
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        break

            else:  
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


            if return_button.collidepoint(pygame.mouse.get_pos()) and not(add_word_button.collidepoint(pygame.mouse.get_pos())):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    usr_word = ""
                    break
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

        pygame.display.flip()  
        clock.tick(60) 

    if usr_word != "":
        add_word(usr_word)


def popup(screen, clock, my_fonts, mouseclicked, text, text_pos):

    # Rendering 
        
    screen_fade = pygame.Surface((800, 800))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))
        
    pygame.draw.rect(screen, (255, 255, 255), (100, 250, 600, 300))
    text_display = my_fonts[1].render(text, True, (0, 0, 0))
    screen.blit(text_display, text_pos)

    pygame.draw.rect(screen, (168, 168, 168), (295, 450, 203, 80))
    ok_button = pygame.Rect((295, 450, 203, 80))
    ok_button_text = my_fonts[0].render("OK", True, (0, 0, 0))
    screen.blit(ok_button_text, (370, 470))

    pygame.display.flip()  
    clock.tick(60)

    # Logic

    if ok_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return True