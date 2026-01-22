# Libraries

import os

# Variables

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "assets" , "gamedata" ,"scores.txt")

# Functions

def read_scores():
    lines = read_scores_file()

    return lines[4:]

def read_scores_file():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def write_lines(lines):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)

def add_scores(username, score, errors):
    lines = read_scores_file()

    lines.append((username, score, errors))

    write_lines(lines)

def clear_cores():
    lines = read_scores_file()

    write_lines(lines[:4])

def read_username():
    lines = read_scores_file()

    return lines[1]

def change_username(username):
    lines = read_scores_file()

    lines[1] = username

    write_lines(lines)

def check_empty_last_line_scores():
    lines = read_scores_file()
    write_lines(lines)