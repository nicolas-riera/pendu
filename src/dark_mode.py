def light_dark_mode(screen, is_dark_mode):
    
    if is_dark_mode:
        screen_fill_color = (0, 0, 0) 
        text_color = (255, 255, 255)

    else:
        screen_fill_color = (0, 0, 0) 
        text_color = (0, 0, 0)

    return screen_fill_color, text_color

