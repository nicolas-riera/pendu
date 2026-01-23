# Libraries

from src.gamedata_path import *

# Variables

FILE_PATH = get_gamedata_path("config.txt")

# Functions

def read_config_file():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
    
def write_lines(lines):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def default_config():
    write_lines(["is_dark_mode = False"])

def check_empty_last_line_config():
    lines = read_config_file()
    write_lines(lines)