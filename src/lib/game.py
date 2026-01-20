import random


life = 10
word_list = ["home", "street", "food", "sky"]
char_found = ""
solution = random.choice(word_list)

while life > 0 :
    try:

        choice = input("choice a character :")
        if len(choice) != 1 or not choice.isalpha():
            print("wrong choice! put on character")
            continue

        if solution.find(choice) != -1:
            
            occurrences = solution.count(choice)
            
            char_found += choice * occurrences
            print("good choice!")
            print(char_found)
        else:
            life -= 1
            print("ops minus one!")
            print(life)

        if len(solution) == len(char_found):
            print("good job! you win")
            break


        if life <= 0:
            print("you lose !")
            break


        
    
    except KeyboardInterrupt:
        print("\nstopped by user!")
        break
