# Libraries

import pygame
import os

from src.render_adaptive_text import *
from src.keyboard_input import *
from src.dark_mode import *

# Variables

FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "assets", "font", "LiberationSans-Regular.ttf")

# Functions

def ok_popup(screen, my_fonts, mouseclicked, text, text_pos, is_dark_mode):

    # Rendering 
        
    screen_fade = pygame.Surface((800, 800))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))

    screen_fill_color, text_color = light_dark_mode(is_dark_mode)

    if is_dark_mode:
        background_popup_color = (20, 20, 20)
    else:
        background_popup_color = (255, 255, 255)
        
    pygame.draw.rect(screen, background_popup_color, (100, 250, 600, 300))

    text_display = my_fonts[1].render(text, True, text_color)
    screen.blit(text_display, text_pos)

    pygame.draw.rect(screen, (168, 168, 168), (295, 450, 203, 80))
    ok_button = pygame.Rect((295, 450, 203, 80))
    ok_button_text = my_fonts[0].render("OK", True, (0, 0, 0))
    screen.blit(ok_button_text, (370, 470))

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

def replay_menu_popup(screen, my_fonts, mouseclicked, text, text_pos, is_dark_mode, subtitle=False):

    usr_choice = 0
    loop_locker = True

    # Rendering 

    screen_fill_color, text_color = light_dark_mode(is_dark_mode)
        
    screen_fade = pygame.Surface((800, 800))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))

    if is_dark_mode:
        background_popup_color = (20, 20, 20)
    else:
        background_popup_color = (255, 255, 255)
        
    pygame.draw.rect(screen, background_popup_color, (100, 250, 600, 300))

    text_display = my_fonts[1].render(text, True, text_color)
    screen.blit(text_display, text_pos)

    if subtitle:
        render_adaptive_text(
            screen,
            subtitle,
            400,
            400,
            500,
            FONT_PATH,
            centered=True,
            color=text_color
            )

    pygame.draw.rect(screen, (236, 179, 101), (160, 450, 203, 80))
    replay_button = pygame.Rect((160, 450, 203, 80))
    replay_button_text = my_fonts[0].render("Rejouer", True, (0, 0, 0))
    screen.blit(replay_button_text, (205, 470))

    pygame.draw.rect(screen, (236, 179, 201), (430, 450, 203, 80))
    gotomenu_button = pygame.Rect((430, 450, 203, 80))
    gotomenu_button_text = my_fonts[0].render("Menu", True, (0, 0, 0))
    screen.blit(gotomenu_button_text, (495, 470))

    # Logic

    if replay_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            usr_choice = 1
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    elif gotomenu_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            usr_choice = 2
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return loop_locker, usr_choice

def username_input_popup(screen, my_fonts, mouseclicked, usr_word, is_dark_mode):

    # Rendering 

    screen_fill_color, text_color = light_dark_mode(is_dark_mode)
        
    screen_fade = pygame.Surface((800, 800))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))

    if is_dark_mode:
        background_popup_color = (20, 20, 20)
    else:
        background_popup_color = (255, 255, 255)
        
    pygame.draw.rect(screen, background_popup_color, (50, 150, 700, 450))

    text_display = my_fonts[1].render("Entrez votre nom :", True, text_color)
    screen.blit(text_display, (194, 210))

    pygame.draw.rect(screen, (240, 240, 240), (70, 340, 660, 60))
    usr_word_display = my_fonts[0].render(usr_word, True, (0, 0, 0))
    screen.blit(usr_word_display, (75, 350))

    if usr_word == "":  
        ok_button_color = (168, 168, 168)
    else:
        ok_button_color = (236, 179, 101)

    pygame.draw.rect(screen, ok_button_color, (295, 500, 203, 80))
    ok_button = pygame.Rect((295, 500, 203, 80))
    ok_button_text = my_fonts[0].render("OK", True, (0, 0, 0))
    screen.blit(ok_button_text, (370, 520))

    # Logic

    if ok_button.collidepoint(pygame.mouse.get_pos()) and usr_word != "":
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    elif usr_word != "":
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return True
