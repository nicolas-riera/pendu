# Libraries

import pygame
import os

from src.render_adaptive_text import *
from src.keyboard_input import *
from src.dark_mode import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "../", "assets", "font", "LiberationSans-Regular.ttf")

# Assets loading

# Python loads this first, so mixer init has to be here
pygame.mixer.init()

MENU_BUTTON_CLICK_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "menu_button_click_sfx.wav"))
MENU_BUTTON_START_SFX = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "menu_button_start_sfx.mp3"))

# Functions

def ok_popup(screen, my_fonts, mouseclicked, text, text_pos, is_dark_mode):

    '''
    Pygame ok popup loop, returns a boolean 
    to set its state in the loop where it's called.
    By default it returns True so at the next clock round, 
    it can be called and displayed again. When clicking ok, it returns False
    so it's not called again.
    ### PARAMETERS
            screen: pygame.Surface
            my_fonts: tuple[pygame.Font, pygame.Font]
            mouseclicked: bool
            text: str
            text_pos: tuple(int,int,int)
            is_dark_mode: bool
    ### RETURNS
            bool
    '''

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
            pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
            return False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return True

def replay_menu_popup(screen, my_fonts, mouseclicked, text, text_pos, is_dark_mode, subtitle=False):

    '''
    Pygame replay popup menu loop.
    It returns a loop_locker boolean 
    to set its state in the loop where it's called.
    By default it returns True so at the next clock round, 
    it can be called and displayed again. When a choice is made,
    loop_locker is set to False so it's not called again.
    The choice index is returned with loop_locker.
    ### PARAMETERS
            screen: pygame.Surface
            my_fonts: tuple[pygame.Font, pygame.Font]
            mouseclicked: bool
            text: str
            text_pos: tuple(int,int,int)
            is_dark_mode: bool
            subtitle: bool
    ### RETURNS
            loop_locker: bool
            usr_choice: int
    '''

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
            pygame.mixer.Sound.play(MENU_BUTTON_START_SFX)
            usr_choice = 1
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    elif gotomenu_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
            usr_choice = 2
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return loop_locker, usr_choice

def username_input_popup(screen, my_fonts, mouseclicked, usr_word, is_dark_mode):

    '''
    Pygame username input popup loop, returns a boolean 
    to set its state in the loop where it's called.
    By default it returns True so at the next clock round, 
    it can be called and displayed again. When clicking ok, it returns False
    so it's not called again. The real input is handled outside of this function.
    ### PARAMETERS
            screen: pygame.Surface
            my_fonts: tuple[pygame.Font, pygame.Font]
            mouseclicked: bool
            usr_word: str
            is_dark_mode: bool
    ### RETURNS
            bool
    '''

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
            pygame.mixer.Sound.play(MENU_BUTTON_CLICK_SFX)
            return False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    elif usr_word != "":
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return True
