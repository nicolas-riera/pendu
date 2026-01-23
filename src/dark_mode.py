# Libraries

from src.config import *

# Functions

def dark_mode_setting(mode, is_dark_mode):
    lines = read_config_file()

    if mode == "read":
        if lines[0] == "is_dark_mode = True":
            return True
        else:
            return False

    else:
        if is_dark_mode:
            lines[0] = "is_dark_mode = True"
        else:
            lines[0] = "is dark_mode = False"
            
        write_lines(lines)

def check_empty_last_line_config():
    lines = read_config_file()
    write_lines(lines)

def light_dark_mode(screen, is_dark_mode):
    
    if is_dark_mode:
        screen_fill_color = (0, 0, 0) 
        text_color = (255, 255, 255)

    else:
        screen_fill_color = (255, 255, 255) 
        text_color = (0, 0, 0)

    return screen_fill_color, text_color

