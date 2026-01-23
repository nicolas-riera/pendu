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

LETTER_WRITE_SFX_1 = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "letter_write_sfx_1.mp3"))
LETTER_WRITE_SFX_2 = pygame.mixer.Sound(os.path.join(BASE_DIR, "../", "assets", "sfx", "letter_write_sfx_2.mp3"))

# Functions

def make_clue(word_to_guess, letters_found="", letters_tried=""):

    '''
    Take a word to guess and return the corresponding clue. 
    Initialize letters_found and letters_tried because the first letter is given.
    If the first letter is repeated in the word, its also given in the rest of the word.
    Hyphens is given.
    #### For example: 
            1. "Umbrella" will output "U _ _ _ _ _ _ _" clue.
            2. "Example" will output "E _ _ _ _ _ E" clue.
            3. "Science-fiction" will output "S _ _ _ _ _ _ - _ _ _ _ _ _ _" clue.        
    ### PARAMETERS
            word_to_guess: str - litterally the word to guess.
            letters_found: str - letters already found by user.
            letters_tried: str - letters already tried by user.
    ### RETURNS
            clue: str - the clue returned.
            letters_found: str - letters already found by user now containing first letter.
            letters_tried: str - letters already tried by user now containung first letter.
    '''
    
    clue = ""

    for i in range(len(word_to_guess)):
        if i == 0 and len(word_to_guess) > 4:
            clue += word_to_guess[0]
            add_to_letters_tried = check_letter(word_to_guess, normalizing_str(word_to_guess[0]), letters_found, letters_tried)
            letters_found, letters_tried = add_to_letters_tried[1], add_to_letters_tried[2]
        elif normalizing_str(word_to_guess[i]) == normalizing_str(word_to_guess[0]) and len(word_to_guess) > 4:
            clue += word_to_guess[i]
        elif word_to_guess[i] == "-":
            clue += "-"
        else:
            clue += "_"

    return clue, letters_found, letters_tried

def is_in_letters_tried(letter, letters_tried, letters_found):

    '''
    Check if a letter is already found or tried.
    ### PARAMETERS
            letter: str - letter provided by the user.
            letters_tried: str - letters already tried by the user.
            letters_found: str - letters already found by the user.
    ### RETURNS
            bool
    '''

    if letter in letters_tried or letter in letters_found:
        return True
    else:
        return False

def update_clue(clue, letter, word_to_guess, word_to_guess_normalized):

    '''
    Update clue with found letter. The user only provide unaccentuated letters.
    The check is made on unaccentuated word to guess version letters.
    The clue is updated with accentuated word to guess version letters.
    ### For example: 
            word_to_guess = "hélicoptère"
            word_to_guess_normalized = "helicoptere"
            letter = "e"
            clue = "h__________"
            update_clue(clue,letter,word_to_guess,word_to_guess_normalized) -> "hé_____è_e" 
    ### PARAMETERS
            clue: str
            letter: str - the letter found.
            word_to_guess: str - the word to guess.
            word_to_guess_normalized: str - the word to guess without accentuation.
    ### RETURNS
            clue: str
    '''

    clue_list = list(clue)

    for i in range(len(word_to_guess)):
        if letter == word_to_guess_normalized[i]:
            clue_list[i] = word_to_guess[i]
    
    return ''.join(clue_list)

def check_letter(word_to_guess, letter, letters_found, letters_tried):

    '''
    Check if the letter is present in the word to guess.
    ### For example: 
            word_to_guess = "avion"
            letter = "v"
            letters_found = "in"
            letters_tried = "xb"
            check_letter(word_to_guess, letter, letters_found, letters_tried) -> True,"inv","xb"
    ### PARAMETERS
            word_to_guess: str
            letter: str
            letters_found: str
            letters_tried: str
    ### RETURNS
            bool - True if letter in word_to_guess
            letters_tried: str
            letters_found: str
    '''

    if word_to_guess.find(letter) != -1:
        occurrences = word_to_guess.count(letter) 
        letters_found += letter * occurrences
        return True, letters_found, letters_tried
    else:
        letters_tried += letter

    return False, letters_found, letters_tried

def format_str(string_to_format):

    '''
    Add spaces between string_to_format letters.
    ### For example: 
            string_to_format = "hjdsaq"
            format_clue(string_to_format) -> "h j d s a q"
    ### PARAMETERS
            string_to_format: str
    ### RETURNS
            formatted_string: str
    '''

    formatted_string = ""
    for letter in string_to_format:
        formatted_string += f" {letter}"
    return formatted_string

def normalizing_str(string_to_normalize):

    '''
    Normalize its parameter.
    ### For example: 
            string_to_normalize = "Aéronautique"
            normalizing_str(string_to_normalize) -> "aeronautique"
    ### PARAMETERS
            string_to_normalize: str
    ### RETURNS
            str
    '''

    normalized = unicodedata.normalize('NFD', string_to_normalize)
    return "".join(c for c in normalized if unicodedata.category(c) != 'Mn')

def game_won_check(clue, word_to_guess):

    '''
    Check if player won.
    ### For example: 
            clue = "Gateau"
            word_to_guess = "Gateau"
            game_won_check(clue, word_to_guess) -> True
    ### PARAMETERS
            clue: str
            word_to_guess: str
    ### RETURNS
            bool
    '''

    if clue == word_to_guess:
        return True
    else:
        return False
    
def reset_values():

    '''
    Reset game values.
    ### RETURNS
            life: int
            word_to_guess: str
            word_to_guess_normalized: str
            clue: str
            letters_found: str
            letters_tried: str
            letter_checked: bool - game status to know if letter as been checked
            notice_win_popup: bool - status to know if popup is displayed 
            notice_lose_popup: bool - status to know if popup is displayed
            display_text_good_choice: bool - status to know if text is displayed
            display_text_wrong_choice: bool - status to know if text is displayed
            display_text_tried_letter: bool  - status to know if text is displayed
    '''

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

    '''
    Pygame gameplay loop.
    ### PARAMETERS
            screen: pygame.Surface
            clock: pygame.Clock
            my_fonts: tuple[pygame.Font, pygame.Font]
    '''

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
            format_str(clue.capitalize()),
            400,
            180,
            600,
            FONT_PATH,
            centered=True,
            color=text_color
        )

        letters_tried_title_text = my_fonts[0].render("Lettres déjà essayées :", True, text_color)
        screen.blit(letters_tried_title_text, (60, 270))
        letters_tried_text = my_fonts[0].render(format_str(letters_tried.upper()), True, text_color)
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