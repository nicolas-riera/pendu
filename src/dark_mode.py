def light_dark_mode(screen, is_dark_mode):
    
    if not is_dark_mode:
        screen.fill("white")
        text_color = (0, 0, 0)

    else:
        screen.fill((0, 0, 0))
        text_color = (255, 255, 255)

    return text_color

