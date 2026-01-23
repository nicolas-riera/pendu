
def is_dark_modes(screen, is_dark_mode):
    
    if not is_dark_mode:
        screen.fill("white")
        text_color = (0, 0, 0)

    else:
        screen.fill((0, 0, 0))
        text_color = (255, 255, 255)

    return is_dark_mode, text_color

