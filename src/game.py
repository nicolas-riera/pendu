# Libraries

import random
import pygame
import unicodedata
import time

from src.words_mgt import *
from src.pygame_events import *
from src.keyboard_input import *
from src.render_adaptive_text import *
from src.popup import *
from src.dark_mode import *
from src.scores_mgt import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "../", "assets", "font", "LiberationSans-Regular.ttf")

# Assets loading

HANGMAN_IMG = tuple(
    pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "hangman", f"{i}.png"))
    for i in range(7))

HANGMAN_IMG_INVERTED = tuple(
    invert_surface(pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "hangman", f"{i}.png")))
    for i in range(7))

# Functions

def make_clue(word_to_guess, letters_found="", letters_tried=""):

    '''
    Take word_to_guess
    and return a string of the lengh of word_to_guess but filled with "_" and its associated values
    '''
    
    clue = ""

    for i in range(len(word_to_guess)):
        if i == 0 and len(word_to_guess) > 4:
            clue += word_to_guess[0]
            add_to_letters_tried = check_letter(word_to_guess, normalizing_str(word_to_guess[0]), letters_found, letters_tried)
            letters_found, letters_tried = add_to_letters_tried[1], add_to_letters_tried[2]
        elif normalizing_str(word_to_guess[i]) == normalizing_str(word_to_guess[0]):
            clue += word_to_guess[i]
        elif word_to_guess[i] == "-":
            clue += "-"
        else:
            clue += "_"

    return clue, letters_found, letters_tried

def is_in_letters_tried(letter, letters_tried, letters_found):

    '''
    Take letter and letters_tried as parameter 
    and return a boolean if the letter is found in letters_tried or not
    '''


    if letter in letters_tried or letter in letters_found:
        return True
    else:
        return False

def update_clue(clue, letter, word_to_guess, word_to_guess_normalized):

    '''
    Update clue if letter is found in word_to_guess
    '''

    clue_list = list(clue)

    for i in range(len(word_to_guess)):
        if letter == word_to_guess_normalized[i]:
            clue_list[i] = word_to_guess[i]
    
    return ''.join(clue_list)

def return_clue_string(clue):

    clue_string = ''
    for char in clue:
        clue_string = clue_string + ' ' + char

    return clue_string

def check_letter(word_to_guess, letter, letters_found, letters_tried):

    '''
    Check if letter is present in word_to_guess, 
    return is_good_choice, letters_tried and a boolean letter_found
    '''

    if word_to_guess.find(letter) != -1:
        occurrences = word_to_guess.count(letter) 
        letters_found += letter * occurrences
        return True, letters_found, letters_tried
    else:
        letters_tried += letter

    return False, letters_found, letters_tried

def str_already_tried_letters(letters_tried):

    '''
    return stringified letters_tried 
    '''

    str_letters_tried = ""
    for letter in letters_tried:
        str_letters_tried += f" {letter}"
    return str_letters_tried

def normalizing_str(string):

    '''
    Create a version of string without accents
    '''

    normalized = unicodedata.normalize('NFD', string)
    return "".join(c for c in normalized if unicodedata.category(c) != 'Mn')

def game_won_check(clue, word_to_guess):

    '''
    Check if the player has won, 
    return a boolean corresponding if he won or not
    '''

    if clue == word_to_guess:
        return True
    else:
        return False
    
def reset_values():

    life = 6
    word_to_guess = random.choice(read_words())
    word_to_guess_normalized = normalizing_str(word_to_guess)
    clue, letters_found, letters_tried = make_clue(word_to_guess)
    letter_checked = True
    notice_win_popup = False
    notice_lose_popup = False
    display_text_good_choice = False
    display_text_wrong_choice = False 
    display_text_tried_letter = False   
    
    return life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup, display_text_good_choice, display_text_wrong_choice, display_text_tried_letter

def game(screen, clock, my_fonts, is_dark_mode):

    gaming = True
    life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup, display_text_good_choice, display_text_wrong_choice, display_text_tried_letter = reset_values() 

    while gaming:
            
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen_fill_color, text_color = light_dark_mode(is_dark_mode)

        screen.fill(screen_fill_color)

        render_adaptive_text(
            screen,
            return_clue_string(clue.capitalize()),
            400,
            180,
            600,
            FONT_PATH,
            centered=True,
            color=text_color
        )

        letters_tried_title_text = my_fonts[0].render("Lettres déjà essayées :", True, text_color)
        screen.blit(letters_tried_title_text, (60, 270))
        letters_tried_text = my_fonts[0].render(str_already_tried_letters(letters_tried.upper()), True, text_color)
        screen.blit(letters_tried_text, (60, 370))

        if is_dark_mode:
            hangman_title_rect = HANGMAN_IMG_INVERTED[6-life].get_rect(center=(630, 500))
            hangman_title_scaled = pygame.transform.scale(HANGMAN_IMG_INVERTED[6-life], (HANGMAN_IMG_INVERTED[6-life].get_size()[0]*1, HANGMAN_IMG_INVERTED[6-life].get_size()[1]*1))
            screen.blit(hangman_title_scaled, hangman_title_rect)
        else:
            hangman_title_rect = HANGMAN_IMG[6-life].get_rect(center=(630, 500))
            hangman_title_scaled = pygame.transform.scale(HANGMAN_IMG[6-life], (HANGMAN_IMG[6-life].get_size()[0]*1, HANGMAN_IMG[6-life].get_size()[1]*1))
            screen.blit(hangman_title_scaled, hangman_title_rect)

        # Display text rendering

        display_text_y = 770

        if display_text_good_choice and not(notice_win_popup or notice_lose_popup):
            render_adaptive_text(
            screen,
            "Bonne pioche !",
            400,
            display_text_y,
            700,
            FONT_PATH,
            centered=True,
            color=text_color
            )
            
            if time.monotonic() - display_text_timestamp >= 1.0:
                display_text_good_choice = False

        elif display_text_wrong_choice and not(notice_win_popup or notice_lose_popup):
            render_adaptive_text(
            screen,
            "Mauvaise pioche !",
            400,
            display_text_y,
            700,
            FONT_PATH,
            centered=True,
            color=text_color
            )

            if time.monotonic() - display_text_timestamp >= 1.0:
                display_text_wrong_choice = False
                
        elif display_text_tried_letter and not(notice_win_popup or notice_lose_popup):
            render_adaptive_text(
            screen,
            "Lettre déjà essayée...",
            400,
            display_text_y,
            700,
            FONT_PATH,
            centered=True,
            color=text_color
            )

            if time.monotonic() - display_text_timestamp >= 1.0:
                display_text_tried_letter = False


        elif not(notice_win_popup or notice_lose_popup):
            render_adaptive_text(
            screen,
            "Entrez une lettre.",
            400,
            display_text_y,
            700,
            FONT_PATH,
            centered=True,
            color=text_color
            )
        
        # Logic

        if escpressed:
            break

        elif notice_win_popup:
            if time.monotonic() - popup_delay >= 0.7:
                notice_win_popup, usr_choice = replay_menu_popup(screen, my_fonts, mouseclicked, "Vous avez gagné !", (195, 315), is_dark_mode)
                if usr_choice == 1:
                    add_scores(read_username(), word_to_guess, 6-life)
                    life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup, display_text_good_choice, display_text_wrong_choice, display_text_tried_letter = reset_values() 
                elif usr_choice == 2:
                    add_scores(read_username(), word_to_guess, 6-life)
                    gaming = False


        elif notice_lose_popup:
            if time.monotonic() - popup_delay >= 0.7:
                notice_lose_popup, usr_choice = replay_menu_popup(screen, my_fonts, mouseclicked, "Vous avez perdu...", (195, 315), is_dark_mode, subtitle=f"Le mot était {word_to_guess}.")
                if usr_choice == 1:
                    life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup, display_text_good_choice, display_text_wrong_choice, display_text_tried_letter = reset_values() 
                elif usr_choice == 2:
                    gaming = False

        else:

            # Keyboard input logic

            usr_input = keyboard_input(events).lower()

            usr_input_normalized = normalizing_str(usr_input)

            if is_in_letters_tried(usr_input_normalized, letters_tried, letters_found) and usr_input != "":
                display_text_good_choice = False
                display_text_wrong_choice = False
                display_text_tried_letter = True
                display_text_timestamp = time.monotonic()

            elif usr_input != "backspace" and usr_input != "enter" and usr_input != "-" and usr_input != "":
                letter_checked = False

            if not letter_checked:

                is_good_choice, letters_found, letters_tried = check_letter(word_to_guess_normalized, usr_input_normalized, letters_found, letters_tried)
                
                if is_good_choice:
                    clue = update_clue(clue, usr_input_normalized, word_to_guess, word_to_guess_normalized)
                    display_text_good_choice = True
                    display_text_wrong_choice = False
                    display_text_tried_letter = False
                    display_text_timestamp = time.monotonic()
                else:
                    display_text_good_choice = False
                    display_text_wrong_choice = True
                    display_text_tried_letter = False
                    display_text_timestamp = time.monotonic()
                    life -= 1

                letter_checked = True

        if game_won_check(clue, word_to_guess) and not (notice_win_popup or notice_lose_popup):
            notice_win_popup = True
            popup_delay = time.monotonic()
        
        if life == 0 and not (notice_win_popup or notice_lose_popup):
            notice_lose_popup = True
            popup_delay = time.monotonic()

        pygame.display.flip()  
        clock.tick(60)   