# Libraries

from src.gamedata_path import *

# Variables

FILE_PATH = get_gamedata_path("config.txt")

# Functions

def read_config_file():

    '''
    Read the config file from the file path FILE_PATH found in /src/config.py file.
    For now only contains dark mode state
    ### RETURN
            [str]
    '''

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
    
def write_lines(lines):

    '''
    Write lines in the config file from the file path FILE_PATH found in /src/config.py file.
    ### PARAMETER
            lines: str  
    '''

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def default_config():
    
    '''
    Set the default config in config file.
    '''

    write_lines(["is_dark_mode = False"])

def check_empty_last_line_config():

    '''
    Check if config file last line is empty.
    Create one empty last line if none is found.
    '''

    lines = read_config_file()
    write_lines(lines)