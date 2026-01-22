# Libraries

import os

# Variables

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "assets" , "gamedata" ,"words.txt")

# Functions

def read_words():
    lines = read_words_file()

    return lines[103:]
   
def read_words_file():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def write_lines(lines):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def add_word(word):
    lines = read_words_file()

    lines.append(word)

    write_lines(lines)

def remove_word(index):
    lines = read_words_file()

    lines.pop(103 + index)

    write_lines(lines)

def reset_words():
    lines = read_words_file()

    lines = lines[:103] + lines[1:101] 

    write_lines(lines)

def clear_words():
    lines = read_words_file()

    lines = lines[:103]

    write_lines(lines)
    
def check_empty_last_line():
    lines = read_words_file()
    write_lines(lines)
