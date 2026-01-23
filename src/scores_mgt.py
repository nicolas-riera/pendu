# Libraries

import ast

from src.gamedata_path import *

# Variables

FILE_PATH = get_gamedata_path("scores.txt")

# Functions

def read_scores():

    '''
    Read the scores from read_scores_file().
    And parse elements into list of strings tuples
    ### RETURNS
            [(str,str,str)]
    '''

    lines = read_scores_file()

    return [ast.literal_eval(line) for line in lines[4:] if line.strip()]

def read_scores_file():

    '''
    Read the scores file from the file path FILE_PATH found in /src/score_mgt.py file.
    ### RETURNS
            [str]
    '''

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def write_lines(lines):

    '''
    Write lines in the scores file from the file path FILE_PATH found in /src/score_mgt.py file.
    ### PARAMETERS
            lines: str
    '''

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def add_scores(username, score, errors):

    '''
    Add score to the scores.txt file.
    ### PARAMETERS
            username: str
            score: str
            errors: int  
    '''
        
    lines = read_scores_file()

    lines.append((username, score, errors))

    write_lines(lines)

def clear_scores():

    '''
    Clear the scores.txt file scores avoiding clearing username.
    '''

    lines = read_scores_file()

    write_lines(lines[:4])

def read_username():

    '''
    Read username from scores.txt file
    ### RETURNS
            str  
    '''

    lines = read_scores_file()

    return lines[1]

def change_username(username):

    '''
    Change username in the scores.txt file.
    ### PARAMETERS
            lines: str  
    '''

    lines = read_scores_file()

    lines[1] = username

    write_lines(lines)

def check_empty_last_line_scores():

    '''
    Check if scores.txt file last line is empty.
    Create one empty last line if none is found.
    '''

    lines = read_scores_file()
    write_lines(lines)