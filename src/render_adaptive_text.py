# Libraries

import pygame

# Functions

def render_adaptive_text(
    screen,
    text,
    x,
    y,
    max_width,
    font_path,
    max_size=30,
    min_size=12,
    color=(0, 0, 0),
    clickable=False,
    centered=False
):
    
    '''
    Render adaptative text depending on the max width provided.
    ### PARAMETERS
            screen: pygame.Surface
            text: str
            x: int - x position in pixel from top left
            y: int - y position in pixel from top left
            max_size: int
            max_width: int
            color: tuple(int, int, int)
            clickable: bool
            centered: bool
    ### RETURN
            rect: python.Rect
    '''

    size = max_size
    font = pygame.font.Font(font_path, size)
    text_surface = font.render(text, True, color)

    while text_surface.get_width() > max_width and size > min_size:
        size -= 1
        font = pygame.font.Font(font_path, size)
        text_surface = font.render(text, True, color)

    if centered:
        rect = text_surface.get_rect(center=(x, y))
    else:
        rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, rect)

    if clickable:
        return rect
    return