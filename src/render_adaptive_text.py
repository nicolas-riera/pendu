# Libraries

import pygame

# Functions

def render_adaptive_text(
    screen,
    text,
    x,
    y,
    max_width,
    FONT_PATH,
    max_size=30,
    min_size=12,
    color=(0, 0, 0),
    clickable=False,
    centered=False
):
    size = max_size
    font = pygame.font.Font(FONT_PATH, size)
    text_surface = font.render(text, True, color)

    while text_surface.get_width() > max_width and size > min_size:
        size -= 1
        font = pygame.font.Font(FONT_PATH, size)
        text_surface = font.render(text, True, color)

    if centered:
        rect = text_surface.get_rect(center=(x, y))
    else:
        rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, rect)

    if clickable:
        return rect
    return