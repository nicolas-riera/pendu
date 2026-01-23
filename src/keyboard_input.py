# Libraries

import pygame
import unicodedata

# Functions

def keyboard_input(events):

    '''
    Translate in a more friendly way keyboard inputs selected pygame events.
    All events other than backspace, enter and letters are ignored.
    #### For example: 
            1. pygame.K_BACKSPACE turns into "backspace".
            2. pygame.K_RETURN turns into "enter"       
    ### PARAMETERS
            events: pygame.Events
    ### RETURNS
            str
    '''

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return "backspace"
            elif event.key == pygame.K_RETURN:
                return "enter"
            elif event.unicode:
                char = event.unicode
                if char == "-":
                    return char
                if unicodedata.category(char).startswith("L"):  
                    return char
    return ""