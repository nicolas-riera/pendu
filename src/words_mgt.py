# Libraries

from src.gamedata_path import *

# Variables

FILE_PATH = get_gamedata_path("words.txt")

# Functions

def read_words():

    '''
    Read the words from read_words_file().
    And parse words into list of strings
    ### RETURNS
            [str]
    '''

    lines = read_words_file()

    return lines[103:]
   
def read_words_file():

    '''
    Read the words file from the file path FILE_PATH found in /src/words_mgt.py file.
    ### RETURNS
            [str]
    '''

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def write_lines(lines):

    '''
    Write lines in the scoreswords file from the file path FILE_PATH found in /src/words_mgt.py file.
    ### PARAMETERS
            lines: str
    '''

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def add_word(word):

    '''
    Add word to the words.txt file.
    ### PARAMETERS
            word: str 
    '''

    lines = read_words_file()

    lines.append(word)

    write_lines(lines)

def remove_word(index):

    '''
    Remove word from words.txt file using its index.
    ### PARAMETERS
            index: int 
    '''

    lines = read_words_file()

    lines.pop(103 + index)

    write_lines(lines)

def reset_words():

    '''
    Reset user word list from default word list in words.txt file.
    '''

    lines = read_words_file()

    lines = lines[:103] + lines[1:101] 

    write_lines(lines)

def clear_words():

    '''
    Clear user word list in words.txt file.
    '''

    lines = read_words_file()

    lines = lines[:103]

    write_lines(lines)
    
def check_empty_last_line():
    lines = read_words_file()
    write_lines(lines)