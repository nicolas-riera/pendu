# Libraries

import pygame

# Functions

def pygame_events():

    '''
    Pygame events gate to avoid calling events
    multiple time during pygame loops.
    ### RETURNS
            events: pygame.Event
            mouseclicked: bool
            escpressed: bool
    '''
    
    mouseclicked = False
    escpressed = False

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseclicked = True

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                escpressed = True 

    return events, mouseclicked, escpressed