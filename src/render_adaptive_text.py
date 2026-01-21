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
    color=(0, 0, 0)
):
    size = max_size
    font = pygame.font.Font(font_path, size)
    text_surface = font.render(text, True, color)

    while text_surface.get_width() > max_width and size > min_size:
        size -= 1
        font = pygame.font.Font(font_path, size)
        text_surface = font.render(text, True, color)

    screen.blit(text_surface, (x, y))