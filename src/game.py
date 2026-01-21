import random

word_list = ["home", "street", "food", "sky"]

def update_clue(clue,letter,word_to_guess):
    '''Update clue if letter is found in word_to_guess'''
    for i in range(len(word_to_guess)):
        if letter == word_to_guess[i]:
            clue[i] = letter
    return clue

def display_clue(clue):
    clue_string = ''
    for char in clue:
        clue_string += char
    print(clue_string)

def ask_letter(letters_tried=[]):
    '''Ask letter to user and verify user input.'''
    user_input = ""
    while True:
        user_input = input("Veuillez proposer une lettre:")
        if len(user_input) == 1 and user_input.isalpha():
            if user_input not in letters_tried:
                return user_input
            else:
                print(f"{user_input} a déjà été proposée.")
        else:
            print(f"{user_input} n'est pas une lettre.")
    
def check_letter(word_to_guess,letter,letters_found,letters_tried):
    '''Check if letter is present in word_to_guess, 
        return is_good_choice, letters_tried and a boolean letter_found'''
    is_good_choice = False
    if word_to_guess.find(letter) != -1:
        occurrences = word_to_guess.count(letter) 
        letters_found += letter*occurrences
        is_good_choice = True
    else:
        letters_tried += letter
    return is_good_choice,letters_found,letters_tried

def ask_restart_game(gaming):
    '''Ask user if he wants to play again and return gaming boolean'''
    user_input = ""
    while not (user_input == "o" or user_input == "n"):
        try:
            user_input = str(input("Voulez-vous recommencer? (o/n)").lower())   
        except:
            print("Vous devez renseigner O ou N.")
    if user_input == "o":
        gaming = True
    else:
        gaming = False
    return gaming

def game(word_list):
    gaming = True
    try:
        while gaming:
            life = 10
            letters_found = ""
            letters_tried = ""
            word_to_guess = random.choice(word_list)
            clue = list("-" * len(word_to_guess))
            game_won = False
            print("Nouvelle partie de pendu!")
            print("-"*len(word_to_guess))
            while life > 0 and not game_won:
                    letter = ask_letter(letters_tried)
                    clue = update_clue(clue,letter,word_to_guess)
                    is_good_choice,letters_found,letters_tried = check_letter(word_to_guess,letter,letters_found,letters_tried)
                    if is_good_choice:
                        print("Bonne pioche!")
                        update_clue(clue,letter,word_to_guess)
                        if "-" not in clue:
                            game_won = True
                    else:
                        print("Mauvaise pioche!")
                        life -= 1
                    display_clue(clue)
            if game_won:
                print(f"Bravo vous avez trouvé le mot {word_to_guess}")
            else:
                print(f"Vous avez perdu!")
            gaming = ask_restart_game(gaming)
        print("Merci d'avoir joué au pendu.")
                
    except KeyboardInterrupt:
        print("\nstopped by user!")

game(word_list)
