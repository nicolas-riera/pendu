# Libraries

import os
import pygame
import math

from src.words_mgt import *
from src.pygame_events import *
from src.keyboard_input import *
from src.render_adaptive_text import *
from src.popup import *
from src.dark_mode import *
from src.scores_mgt import *
from src.game import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "../", "assets", "font", "LiberationSans-Regular.ttf")

DRAWING_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "drawing_sfx.mp3"))
ESC_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "esc_sfx.mp3"))
INPUT_POPUP_OPEN_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "input_popup_open_sfx.mp3"))
INPUT_POPUP_CLOSE_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "input_popup_close_sfx.mp3"))
MENU_BUTTON_CLICK_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "menu_button_click_sfx.wav"))
NOTICE_POPUP_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "notice_popup_sfx.mp3"))

# Functions

def options(screen, clock, my_fonts, is_dark_mode):

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        settings_title_button_text = my_fonts[1].render("Options", True, text_color)
        screen.blit(settings_title_button_text, (310, 120))

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 300, 203, 80))
        words_button = pygame.Rect((295, 300, 203, 80))
        words_button_text = my_fonts[0].render("Mots", True, (0, 0, 0))
        screen.blit(words_button_text, (365, 320))

        pygame.draw.rect(screen, (236, 179, 50), (295, 400, 203, 80))
        scores_button = pygame.Rect((295, 400, 203, 80))
        scores_button_text = my_fonts[0].render("Scores", True, (0, 0, 0))
        screen.blit(scores_button_text, (352, 420))

        if is_dark_mode:
            dark_mode_button_background_color = (255, 255, 255)
            dark_mode_button_text_color = (0, 0, 0)
        else:
            dark_mode_button_background_color = (0, 0, 0)
            dark_mode_button_text_color = (255, 255, 255)

        pygame.draw.rect(screen, dark_mode_button_background_color, (295, 500, 203, 80))
        dark_mode_button = pygame.Rect((295, 500, 203, 80))
        dark_mode_button_text = my_fonts[0].render("Clair/Sombre", True, dark_mode_button_text_color)
        screen.blit(dark_mode_button_text, (308, 520))

        pygame.draw.rect(screen, (168, 168, 168), (295, 600, 203, 80))
        return_button = pygame.Rect((295, 600, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 620))

        pygame.display.flip()  
        clock.tick(60)     

        # Logic

        if escpressed:
            pygame.mixer.Sound.play(ESC_SFX)
            break
        
        elif words_button.collidepoint(pygame.mouse.get_pos()) or scores_button.collidepoint(pygame.mouse.get_pos()) or return_button.collidepoint(pygame.mouse.get_pos()) or dark_mode_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if words_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    words_menu(screen, clock, my_fonts, is_dark_mode)
                elif scores_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    scores_menu_options(screen, clock, my_fonts, is_dark_mode)
                elif dark_mode_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    is_dark_mode = not is_dark_mode
                    dark_mode_setting("write", is_dark_mode)
                elif return_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    return is_dark_mode

def words_menu(screen, clock, my_fonts, is_dark_mode):

    reset_popup = False
    
    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()
        
        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        words_title_text = my_fonts[1].render("Mots", True, text_color)
        screen.blit(words_title_text, (340, 120))

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
            pygame.mixer.Sound.play(ESC_SFX)
            break

        elif reset_popup:
            reset_popup = ok_popup(screen, my_fonts, mouseclicked, "La liste a été restaurée.", (150, 315), is_dark_mode)

        else:
            if add_word_button.collidepoint(pygame.mouse.get_pos()) or return_button.collidepoint(pygame.mouse.get_pos()) or add_word_button.collidepoint(pygame.mouse.get_pos()) or remove_word_button.collidepoint(pygame.mouse.get_pos()) or reset_word_button.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if add_word_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        add_word_menu(screen, clock, my_fonts, is_dark_mode)
                    elif return_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        break
                    elif remove_word_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        remove_word_menu(screen, clock, my_fonts, is_dark_mode)
                    elif reset_word_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                        reset_words()
                        reset_popup = True

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)       

        pygame.display.flip()  
        clock.tick(60) 

def add_word_menu(screen, clock, my_fonts, is_dark_mode):

    usr_word = ""
    error_found_popup = False
    error_too_short_popup = False
    error_only_one_letter_popup = False

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Keyboard input logic

        if not(error_found_popup or error_too_short_popup):
            usr_input = keyboard_input(events)

        if usr_input == "backspace":
            usr_word = usr_word[:-1]
        elif usr_input == "enter":
            if usr_word.lower() in read_words():
                if not error_found_popup:
                    pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                error_found_popup = True
            elif len(usr_word.replace("-", "")) < 3:
                if not error_too_short_popup:
                    pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                error_too_short_popup = True
            else:
                error_only_one_letter_popup = True
                for i in range(len(usr_word)):
                    if normalizing_str(usr_word[0]) != normalizing_str(usr_word[i]):
                        error_only_one_letter_popup = False
                if not error_only_one_letter_popup:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    break
                pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
        else:
            if len(usr_word) < 26:
                usr_word += usr_input

        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        words_title_text = my_fonts[1].render("Ajouter un mot", True, text_color)
        screen.blit(words_title_text, (230, 120))

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

        if escpressed:
            pygame.mixer.Sound.play(ESC_SFX)
            usr_word = ""
            break

        elif error_found_popup:
            error_found_popup = ok_popup(screen, my_fonts, mouseclicked, "Le mot existe déjà.", (193, 315), is_dark_mode)
        elif error_too_short_popup:
            error_too_short_popup = ok_popup(screen, my_fonts, mouseclicked, "Le mot est trop court.", (168, 315), is_dark_mode)
        elif error_only_one_letter_popup:
            error_only_one_letter_popup = ok_popup(screen,my_fonts, mouseclicked, "C'est un mot d'une lettre.", (130,315), is_dark_mode)
        
        elif add_word_button.collidepoint(pygame.mouse.get_pos()) and not(return_button.collidepoint(pygame.mouse.get_pos())):
            if usr_word != "":
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if mouseclicked:
                    if usr_word in read_words():
                        error_found_popup = True
                        pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                    elif len(usr_word.replace("-", "")) < 3:
                        error_too_short_popup = True
                        pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                    else:
                        error_only_one_letter_popup = True
                        for i in range(len(usr_word)):
                            if normalizing_str(usr_word[0]) != normalizing_str(usr_word[i]):
                                error_only_one_letter_popup = False
                        if not error_only_one_letter_popup:
                            pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            break
                        pygame.mixer.Sound.play(NOTICE_POPUP_SFX)

            else:  
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if return_button.collidepoint(pygame.mouse.get_pos()) and not(add_word_button.collidepoint(pygame.mouse.get_pos())):
                if mouseclicked:
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
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
        add_word(usr_word.lower())


def remove_word_menu(screen, clock, my_fonts, is_dark_mode):

    words_list = read_words()
    words_list_current_page = 0

    previous_page_rect = None
    next_page_rect = None

    error_popup_empty = False
    notice_clear_all_popup = False
        
    while True:

        clickable_words = []
        words_list_pages = math.ceil(len(words_list) / 20)

        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        words_title_text = my_fonts[1].render("Retirer un mot", True, text_color)
        screen.blit(words_title_text, (233, 22))

        if words_list != []:
            for i in range(words_list_current_page * 20, len(words_list)):
                if (i-words_list_current_page * 20) < 10:
                    word_rect = render_adaptive_text(
                        screen=screen,
                        text=words_list[i].capitalize(),
                        x=130,
                        y=100 + 50 * (i-words_list_current_page * 20),
                        max_width=250,
                        font_path=FONT_PATH,
                        clickable=True,
                        color=text_color
                    )

                    clickable_words.append((words_list[i], word_rect))
                
                elif (i-words_list_current_page * 20) < 20:
                    word_rect = render_adaptive_text(
                        screen=screen,
                        text=words_list[i].capitalize(),
                        x=450,
                        y=100 + 50 * ((i-words_list_current_page * 20)-10),
                        max_width=250,
                        font_path=FONT_PATH,
                        clickable=True,
                        color=text_color
                    )

                    clickable_words.append((words_list[i], word_rect))
                
        if words_list_pages > 1:

            if words_list_current_page != 0:
                previous_page_arrow = my_fonts[1].render("<", True, text_color)
                previous_page_rect = previous_page_arrow.get_rect(topleft=(70, 660))
                screen.blit(previous_page_arrow, (70, 660))
            else:
                previous_page_rect = None

            if words_list_current_page != words_list_pages-1:
                next_page_arrow = my_fonts[1].render(">", True, text_color)
                next_page_rect = next_page_arrow.get_rect(topleft=(700, 660))
                screen.blit(next_page_arrow, (700, 660))
            else:
                next_page_rect = None

        pygame.draw.rect(screen, (168, 168, 168), (165, 650, 203, 80))
        return_button = pygame.Rect((165, 650, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (226, 670))

        pygame.draw.rect(screen, (236, 179, 201), (425, 650, 203, 80))
        delete_all_button = pygame.Rect((425, 650, 203, 80))
        delete_all_button_text = my_fonts[0].render("Tout supprimer", True, (0, 0, 0))
        screen.blit(delete_all_button_text, (427, 670))

        page_indicator_text = my_fonts[0].render(f"Page {words_list_current_page + 1}", True, text_color)
        screen.blit(page_indicator_text, (352, 743))

        # Logic

        hover = False

        if next_page_rect is not None:
            if next_page_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                    words_list_current_page += 1
                else:
                    hover = True   
        
        if previous_page_rect is not None:
            if previous_page_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                    words_list_current_page -= 1
                else:
                    hover = True

        if escpressed:
            pygame.mixer.Sound.play(ESC_SFX)
            break

        elif error_popup_empty:
            error_popup_empty = ok_popup(screen, my_fonts, mouseclicked, "La liste est vide.", (213, 315), is_dark_mode)
            if not error_popup_empty:
                break
        
        elif notice_clear_all_popup:
            notice_clear_all_popup = ok_popup(screen, my_fonts, mouseclicked, "Liste vidée.", (270, 315), is_dark_mode)
            if not notice_clear_all_popup:
                clear_words()
                break

        elif words_list == []:
            pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
            error_popup_empty = True


        elif return_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                break
            else:
                hover = True  

        elif delete_all_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) 
                notice_clear_all_popup = True
            else:
                hover = True
           
        for word, word_rect in clickable_words:
            if word_rect.collidepoint(pygame.mouse.get_pos()):
                if not notice_clear_all_popup:
                   pygame.draw.line(screen, (236, 179, 201), (word_rect.left-8, word_rect.centery), (word_rect.right+8, word_rect.centery), 2)
                if mouseclicked:
                    pygame.mixer.Sound.play(DRAWING_SFX)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    remove_word(words_list.index(word))
                    words_list = read_words()
                    if words_list_pages != math.ceil(len(words_list) / 20) and words_list_current_page + 1 == words_list_pages:
                        words_list_current_page -= 1
                else:
                    if not notice_clear_all_popup:
                        hover = True

        if hover == True:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif not (error_popup_empty or notice_clear_all_popup):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60) 

def scores_menu_options(screen, clock, my_fonts, is_dark_mode):

    reset_popup = False
    notice_username_input_popup = False
    notice_username_input_empty_popup = False
    usr_word = read_username()
    
    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        words_title_button_text = my_fonts[1].render("Scores", True, text_color)
        screen.blit(words_title_button_text, (320, 120))

        # Draw.rect(surface, color, (x position, y position, x width, y width))
        pygame.draw.rect(screen, (236, 179, 101), (295, 300, 203, 80))
        clear_scores_button = pygame.Rect((295, 300, 203, 80))
        clear_scores_button_text = my_fonts[0].render("Vider scores", True, (0, 0, 0))
        screen.blit(clear_scores_button_text, (312, 320))
        
        pygame.draw.rect(screen, (236, 179, 151), (295, 400, 203, 80))
        change_username_button = pygame.Rect((295, 400, 203, 80))
        change_username_button_text = my_fonts[0].render("Changer nom", True, (0, 0, 0))
        screen.blit(change_username_button_text, (305, 420))

        pygame.draw.rect(screen, (168, 168, 168), (295, 600, 203, 80))
        return_button = pygame.Rect((295, 600, 203, 80))
        return_button_text = my_fonts[0].render("Retour", True, (0, 0, 0))
        screen.blit(return_button_text, (356, 620))    

        # Logic

        if escpressed:
            pygame.mixer.Sound.play(ESC_SFX)
            break

        elif reset_popup:
            reset_popup = ok_popup(screen, my_fonts, mouseclicked, "Scores effacés", (230, 315), is_dark_mode)
        elif notice_username_input_popup:
            usr_input = keyboard_input(events)

            if usr_input == "backspace":
                usr_word = usr_word[:-1]
            elif usr_input == "enter":
                if usr_word != "":
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    pygame.mixer.Sound.play(INPUT_POPUP_CLOSE_SFX)
                    notice_username_input_popup = False
                    change_username(usr_word)

                    usr_word = ""
                    continue
                else:
                    notice_username_input_empty_popup = True
            elif len(usr_word) < 26:
                usr_word += usr_input
            
            notice_username_input_popup = username_input_popup(screen, my_fonts, mouseclicked, usr_word, is_dark_mode)

            if notice_username_input_empty_popup:
                notice_username_input_empty_popup = ok_popup(screen, my_fonts, mouseclicked, "Nom vide.", (287, 315), is_dark_mode)

            if not notice_username_input_popup:
                if usr_word != "":
                    pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                    pygame.mixer.Sound.play(INPUT_POPUP_CLOSE_SFX)
                    change_username(usr_word)

                    usr_word = ""
                    continue
                else:
                    notice_username_input_popup = True
                    notice_username_input_empty_popup = True

        else:
            if clear_scores_button.collidepoint(pygame.mouse.get_pos()) or return_button.collidepoint(pygame.mouse.get_pos()) or change_username_button.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if clear_scores_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        pygame.mixer.Sound.play(NOTICE_POPUP_SFX)
                        reset_popup = True
                        clear_scores()
                    elif return_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        break
                    elif change_username_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
                        pygame.mixer.Sound.play(INPUT_POPUP_OPEN_SFX)
                        notice_username_input_popup = True                

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)       

        pygame.display.flip()  
        clock.tick(60) 