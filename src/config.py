# Libraries

import os

# Variables

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "assets" , "gamedata" ,"config.txt")

# Functions

def read_config_file():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
    
def write_lines(lines):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def default_config():
    write_lines(["is_dark_mode = False"])