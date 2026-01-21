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
        return [word[:-1].lower() for word in f.readlines()]
    
def add_word(word:str):
        
    file_list = read_words_file()

    file_list.append(word)

    text_list=""
    for e in file_list:
        text_list += e +"\n"

    with open(FILE_PATH, "w") as f:
        f.write(text_list)

def remove_word(index):

    file_list = read_words_file().pop(18-index)

    text_list=""
    for e in file_list:
        text_list += e +"\n"

    with open(FILE_PATH, "w") as f:
        f.write(text_list)

def reset_words():

    file_list = read_words_file()[:18]

    text_list=""
    for e in file_list:
        text_list += e +"\n"
    for e in file_list[1:16]:
        text_list += e +"\n"

    with open(FILE_PATH, "w") as f:
        f.write(text_list)
        