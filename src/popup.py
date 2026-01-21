# Libraries

import pygame

# Functions

def ok_popup(screen, clock, my_fonts, mouseclicked, text, text_pos):

    # Rendering 
        
    screen_fade = pygame.Surface((800, 800))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))
        
    pygame.draw.rect(screen, (255, 255, 255), (100, 250, 600, 300))
    text_display = my_fonts[1].render(text, True, (0, 0, 0))
    screen.blit(text_display, text_pos)

    pygame.draw.rect(screen, (168, 168, 168), (295, 450, 203, 80))
    ok_button = pygame.Rect((295, 450, 203, 80))
    ok_button_text = my_fonts[0].render("OK", True, (0, 0, 0))
    screen.blit(ok_button_text, (370, 470))

    pygame.display.flip()  
    clock.tick(60)

    # Logic

    if ok_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return True

def replay_menu_popup(screen, clock, my_fonts, mouseclicked, text, text_pos):

    usr_choice = 0
    loop_locker = True

    # Rendering 
        
    screen_fade = pygame.Surface((800, 800))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))
        
    pygame.draw.rect(screen, (255, 255, 255), (100, 250, 600, 300))
    text_display = my_fonts[1].render(text, True, (0, 0, 0))
    screen.blit(text_display, text_pos)

    pygame.draw.rect(screen, (236, 179, 101), (160, 450, 203, 80))
    replay_button = pygame.Rect((160, 450, 203, 80))
    replay_button_text = my_fonts[0].render("Rejouer", True, (0, 0, 0))
    screen.blit(replay_button_text, 218, 470)

    pygame.draw.rect(screen, (236, 179, 201), (430, 450, 203, 80))
    gotomenu_button = pygame.Rect((430, 450, 203, 80))
    gotomenu_button_text = my_fonts[0].render("Menu", True, (0, 0, 0))
    screen.blit(gotomenu_button_text, (500, 470))

    pygame.display.flip()  
    clock.tick(60)

    # Logic

    if replay_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            usr_choice = 1
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    elif gotomenu_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            usr_choice = 2
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return loop_locker, usr_choice