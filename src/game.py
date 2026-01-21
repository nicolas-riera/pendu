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

def is_in_letters_tried(letter,letters_tried,letters_found):

    '''
    Take letter and letters_tried as parameter 
    and return a boolean if the letter is found in letters_tried or not
    '''

    is_tried = False
    if letter in letters_tried:
        is_tried = True
    elif letter in letters_found:
        is_tried = True
    else:
        is_tried = False
    return is_tried

def update_clue(clue,letter,word_to_guess):

    '''
    Update clue if letter is found in word_to_guess
    '''

    for i in range(len(word_to_guess)):
        if letter == word_to_guess[i]:
            clue[i] = letter
    return clue

def return_clue_string(clue):
    clue_string = ''
    for char in clue:
        clue_string = clue_string + ' ' + char
    return clue_string

def check_letter(word_to_guess,letter,letters_found,letters_tried):

    '''
    Check if letter is present in word_to_guess, 
        return is_good_choice, letters_tried and a boolean letter_found
    '''
    
    is_good_choice = False
    if word_to_guess.find(letter) != -1:
        occurrences = word_to_guess.count(letter) 
        letters_found += letter*occurrences
        is_good_choice = True
    else:
        letters_tried += letter
    return is_good_choice,letters_found,letters_tried

def normalizing_letter(usr_input):
    normalized = unicodedata.normalize('NFD', usr_input)
    return ''.join(c for c in normalized if not unicodedata.combining(c))

def game(screen,clock,my_fonts):

    gaming = True

    word_list = read_words()
    life = 10
    letters_found = ""
    letters_tried = ""
    word_to_guess = random.choice(word_list)
    clue = list("_" * len(word_to_guess))
    game_won = False
    letter_checked = True
    notice_win_popup = False
    notice_lose_popup = False

    while gaming:
            
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering  

        screen.fill("white") 

        clue_text = my_fonts[0].render(return_clue_string(clue), True, (0, 0, 0))
        screen.blit(clue_text, (300, 220))   

        # Logic

        if escpressed:
            break

        elif notice_win_popup:
            notice_win_popup, usr_choice = replay_menu_popup(screen, clock, my_fonts, mouseclicked, "Vous avez gagné !", (195, 315))
            if usr_choice == 1:
                life = 10
                letters_found = ""
                letters_tried = ""
                word_to_guess = random.choice(word_list)
                clue = list("_" * len(word_to_guess))
                game_won = False
                letter_checked = True
                notice_win_popup = False
            elif usr_choice == 2:
                gaming = False


        elif notice_lose_popup:
            notice_win_popup, usr_choice = replay_menu_popup(screen, clock, my_fonts, mouseclicked, "Vous avez perdu...", (195, 315))
            if usr_choice == 1:
                life = 10
                letters_found = ""
                letters_tried = ""
                word_to_guess = random.choice(word_list)
                clue = list("_" * len(word_to_guess))
                game_won = False
                letter_checked = True
                notice_lose_popup = False
            elif usr_choice == 2:
                gaming = False

        else:

            # Keyboard input logic

            usr_input = keyboard_input(events).lower()

            if usr_input != "":
                usr_input = normalizing_letter(usr_input)

            letter_tried_already = is_in_letters_tried(usr_input,letters_tried,letters_found)
            
            if usr_input != "backspace" and usr_input != "enter" and usr_input != "-" and usr_input != "" and not letter_tried_already:
                letter = usr_input
                letter_checked = False

            if not letter_checked:
                clue = update_clue(clue,letter,word_to_guess)
                is_good_choice,letters_found,letters_tried = check_letter(word_to_guess,letter,letters_found,letters_tried)
                if is_good_choice:
                    print("Bonne pioche!")
                    update_clue(clue,letter,word_to_guess)
                    if "_" not in clue:
                        game_won = True
                else:
                    print("Mauvaise pioche!")
                    life -= 1
                letter_checked = True

        if game_won and not (notice_win_popup or notice_lose_popup):
            notice_win_popup = True
        else:
            notice_lose_popup = True

        pygame.display.flip()  
        clock.tick(60)   