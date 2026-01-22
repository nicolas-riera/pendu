# Libraries

import random
import pygame
import unicodedata

from src.words_mgt import *
from src.pygame_events import *
from src.keyboard_input import *
from src.render_adaptive_text import *
from src.popup import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "../", "assets", "font", "LiberationSans-Regular.ttf")

# Functions

def make_clue(word_to_guess):
    '''
    Take word_to_guess
    and return a string of the lengh of word_to_guess but filled with "_"
    '''
    
    clue = ""

    for i in range(len(word_to_guess)):
        if i == 0 and len(word_to_guess) > 4:
            clue += word_to_guess[0]
        elif word_to_guess[i] == "-":
            clue += "-"
        else:
            clue += "_"

    return clue

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

    life = 7
    letters_found = ""
    letters_tried = ""
    word_to_guess = random.choice(read_words())
    word_to_guess_normalized = normalizing_str(word_to_guess)
    clue = make_clue(word_to_guess)
    letter_checked = True
    notice_win_popup = False
    notice_lose_popup = False
    
    return life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup

def game(screen,clock,my_fonts):

    gaming = True
    life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup = reset_values() 

    while gaming:
            
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen.fill("white") 

        render_adaptive_text(
            screen,
            return_clue_string(clue),
            400,
            220,
            600,
            FONT_PATH,
            centered=True
        )
        
        # Logic

        if escpressed:
            break

        elif notice_win_popup:
            notice_win_popup, usr_choice = replay_menu_popup(screen, clock, my_fonts, mouseclicked, "Vous avez gagné !", (195, 315))
            if usr_choice == 1:
                life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup = reset_values() 
            elif usr_choice == 2:
                gaming = False


        elif notice_lose_popup:
            notice_lose_popup, usr_choice = replay_menu_popup(screen, clock, my_fonts, mouseclicked, "Vous avez perdu...", (195, 315))
            if usr_choice == 1:
                life, letters_found, letters_tried, word_to_guess, word_to_guess_normalized, clue, letter_checked, notice_win_popup, notice_lose_popup = reset_values() 
            elif usr_choice == 2:
                gaming = False

        else:

            # Keyboard input logic

            usr_input = keyboard_input(events).lower()

            usr_input_normalized = normalizing_str(usr_input)

            if is_in_letters_tried(usr_input_normalized, letters_tried, letters_found):
                # tbd : display text that the letter has already been tried
                pass

            elif usr_input != "backspace" and usr_input != "enter" and usr_input != "-" and usr_input != "":
                letter_checked = False

            if not letter_checked:

                is_good_choice, letters_found, letters_tried = check_letter(word_to_guess_normalized, usr_input_normalized, letters_found, letters_tried)
                
                if is_good_choice:
                    clue = update_clue(clue, usr_input_normalized, word_to_guess, word_to_guess_normalized)
                    # tbd : display that it is a good choice
                else:
                    # tbd : display that it isn't a good choice
                    life -= 1

                letter_checked = True

        if game_won_check(clue, word_to_guess) and not (notice_win_popup or notice_lose_popup):
            notice_win_popup = True
        
        if life == 0:
            notice_lose_popup = True

        pygame.display.flip()  
        clock.tick(60)   