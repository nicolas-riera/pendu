# Libraries

import os

# Variables

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "assets" , "words.txt")

# Functions

def read_words():
    with open(FILE_PATH) as f:
        return [word[:-1].lower() for word in f.readlines()[18:]]
    
def read_words_file():
    with open(FILE_PATH) as f:
        return [word.lower() for word in f.readlines()]
    
def add_word(word:str):
        
    file_list = read_words_file()

    file_list.append(word)

    text_list=""
    for e in file_list:
        text_list += e +"\n"

    with open(FILE_PATH, "w") as f:
        f.write(text_list)

def remove_word(index):

    file_list = read_words_file()
    
    file_list.pop(18+index)

    text_list=""
    for e in file_list:
        text_list += e

    with open(FILE_PATH, "w") as f:
        f.write(text_list)

def reset_words():

    file_list = read_words_file()[:18]

    text_list=""
    for e in file_list:
        text_list += e
    for e in file_list[1:16]:
        text_list += e

    with open(FILE_PATH, "w") as f:
        f.write(text_list)

def check_empty_last_line():

    file_list = read_words_file()
        
    if file_list[len(file_list)-1] != f"{file_list[len(file_list)-1]}\n":
        file_list[len(file_list)-1] = f"{file_list[len(file_list)-1]}\n"
    
    text_list=""
    for e in file_list:
        text_list += e

    with open(FILE_PATH, "w") as f:
        f.write(text_list)