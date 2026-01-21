import random

def display_char(choice, solution, word):

    for i in range(len(solution)):
        if choice == solution[i]:
            word[i] = choice

    print("".join(word))

def check_choice(choice):
    
    if len(choice) != 1 or not choice.isalpha():
        print("wrong choice! put on character")
        return choice
    
def check_accuracy(solution, choice,char_found,word):

    if solution.find(choice) != -1:
            
        occurrences = solution.count(choice)
            
        char_found += choice * occurrences
        print("good choice!")

        display_char(choice,solution,word)
            
    else:
        life -= 1
        print("ops minus one!")   

def win_condition(solution,char_found):

    if len(solution) == len(char_found):
            print("good job! you win")
            
def loose_condition(life):

    if life <= 0:
        print("you lose !")
            




life = 10
word_list = ["home", "street", "food", "sky"]
char_found = ""
solution = random.choice(word_list)
word = list("-" * len(solution))



print("-"*len(solution))

while life > 0 :
    try:
        choice = input("choose a character :")

        check_choice(choice)

        check_accuracy(solution,choice,char_found,word)
            

        win_condition(solution,char_found)

        loose_condition(life)


    except KeyboardInterrupt:
        print("\nstopped by user!")
        break



