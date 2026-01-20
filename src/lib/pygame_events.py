# Libraries

import pygame

# Functions

def pygame_events():

    mouseclicked = False
    echappressed = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = True

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                echappressed = True                     

    return mouseclicked, echappressed