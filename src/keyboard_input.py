# Libraries

import pygame
import unicodedata

# Functions

def keyboard_input(events):
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