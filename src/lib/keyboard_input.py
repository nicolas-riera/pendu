# Libraries

import pygame

# Variables

KEY_TO_LETTER = {
    pygame.K_a: "a",
    pygame.K_z: "z",
    pygame.K_e: "e",
    pygame.K_r: "r",
    pygame.K_t: "t",
    pygame.K_y: "y",
    pygame.K_u: "u",
    pygame.K_i: "i",
    pygame.K_o: "o",
    pygame.K_p: "p",
    pygame.K_q: "q",
    pygame.K_s: "s",
    pygame.K_d: "d",
    pygame.K_f: "f",
    pygame.K_g: "g",
    pygame.K_h: "h",
    pygame.K_j: "j",
    pygame.K_k: "k",
    pygame.K_l: "l",
    pygame.K_m: "m",
    pygame.K_w: "w",
    pygame.K_x: "x",
    pygame.K_c: "c",
    pygame.K_v: "v",
    pygame.K_b: "b",
    pygame.K_n: "n",
    
    pygame.K_BACKSPACE: "backspace",
    pygame.K_RETURN: "enter",
}

# Functions

def keyboard_input(events):

    for event in events:
        if event.type == pygame.KEYDOWN:        
            if event.key in KEY_TO_LETTER:
                return KEY_TO_LETTER[event.key]

    return ""