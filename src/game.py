import random
import pygame
import unicodedata

from src.words_mgt import *
from src.pygame_events import *
from src.keyboard_input import *
from src.render_adaptive_text import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "../", "assets", "font", "LiberationSans-Regular.ttf")



############################## Console only ##############################################
def ask_letter(letters_tried=[]):
    '''Ask letter to user and verify user input.'''
    user_input = ""
    while True:
        user_input = str(input("Veuillez proposer une lettre:"))
        if len(user_input) == 1 and user_input.isalpha():
            if user_input not in letters_tried:
                return user_input
            else:
                print(f"{user_input} a déjà été proposée.")
        else:
            print(f"{user_input} n'est pas une lettre.")
    
def ask_restart_game(gaming):
    '''Ask user if he wants to play again and return gaming boolean'''
    user_input = ""
    while not (user_input == "o" or user_input == "n"):
        try:
            user_input = str(input("Voulez-vous recommencer? (o/n)").lower())   
        except:
            print("Vous devez renseigner O ou N.")
    if user_input == "o":
        gaming = True
    else:
        gaming = False
    return gaming

##########################################################################################

def is_in_letters_tried(letter,letters_tried,letters_found):
    '''Take letter and letters_tried as parameter 
    and return a boolean if the letter is found in letters_tried or not'''
    is_tried = False
    if letter in letters_tried:
        is_tried = True
    elif letter in letters_found:
        is_tried = True
    else:
        is_tried = False
    return is_tried

def update_clue(clue,letter,word_to_guess):
    '''Update clue if letter is found in word_to_guess'''
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
    '''Check if letter is present in word_to_guess, 
        return is_good_choice, letters_tried and a boolean letter_found'''
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
    try:
        while gaming:

            word_list = read_words()
            life = 10
            letters_found = ""
            letters_tried = ""
            word_to_guess = random.choice(word_list)
            clue = list("_" * len(word_to_guess))
            game_won = False
            letter_checked = True
            print("Nouvelle partie de pendu!")
            print("_"*len(word_to_guess))

            while life > 0 and not game_won:
                
                # pygame events

                events, mouseclicked, escpressed = pygame_events()

                # Rendering  

                screen.fill("white") 

                settings_title_button_text = my_fonts[1].render("Game", True, (0, 0, 0))
                screen.blit(settings_title_button_text, (310, 120))

                clue_text = my_fonts[0].render(return_clue_string(clue), True, (0, 0, 0))
                screen.blit(clue_text, (300, 220))

                pygame.display.flip()  
                clock.tick(60)     

                # Logic

                # Keyboard input logic

                usr_input = keyboard_input(events).lower()

                if usr_input != "":
                    usr_input = normalizing_letter(usr_input)

                letter_tried_already = is_in_letters_tried(usr_input,letters_tried,letters_found)
                
                if usr_input != "backspace" and usr_input != "enter" and usr_input != "-" and usr_input != "" and not letter_tried_already:
                    letter = usr_input
                    letter_checked = False

                if escpressed:
                    break
                    
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

            if game_won:
                print(f"Bravo vous avez trouvé le mot {word_to_guess}")
            else:
                print(f"Vous avez perdu!")
            gaming = True
        print("Merci d'avoir joué au pendu.")
                
    except KeyboardInterrupt:
        print("\nstopped by user!")