def light_dark_mode(screen, is_dark_mode):
    
    if is_dark_mode:
        screen.fill((0, 0, 0))
        text_color = (255, 255, 255)

    else:
        screen.fill((255, 255, 255))
        text_color = (0, 0, 0)

    return text_color

