# Libraries

import pygame

# Functions

def pygame_events():

    mouseclicked = False
    escpressed = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = True

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                escpressed = True 

    return mouseclicked, escpressed