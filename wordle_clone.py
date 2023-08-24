from random import randint
import os

WORD_FILE = "parole_5_lettere.txt"
GREEN = "\033[32m"
YELLOW = "\033[33m"

def highlight_text(text, color_code):
    return f"{color_code}{text}\033[0m"


def check_win(guess, correct_word):
    return guess == correct_word


def check_guess_validity(guess, all_words):
    return len(guess) == 5 and guess in all_words


def substitute_letter(index, word, substitute):
    new_word = word[:index] + substitute + word[index+1:]
    return new_word

def print_word(word, word_to_guess):
    index_of_current_word_letter = 0

    for letter in word:
        try:
            real_index_of_letter = word_to_guess.index(letter)  #guardo se la lettera è presente nella parola da indovinare 
            word_to_guess = substitute_letter(real_index_of_letter, word_to_guess, "-") #passo fondamentale per evitare problemi con lettere ripetute
                                    
            if real_index_of_letter == index_of_current_word_letter:
                print(highlight_text(letter, GREEN), end="") #lettera giusta al posto giusto
            else:
                print(highlight_text(letter, YELLOW), end="") #lettera giusta al posto sbagliato

        except ValueError:
            print(letter, end="") #lettera sbagliata

        index_of_current_word_letter += 1


def print_game(words_tried, correct_word):
    os.system("clear")

    print("BENVENUTO NEL CLONE BRUTTO DI WORDLE FATTO DAL FEDE_DES :)")
    print(f"La parola da indovinare ha 5 lettere")
    print("Hai 6 tentativi per indovinare la parola")
    print()
    
    for word in words_tried:
        print_word(word, correct_word)
        print()



if __name__ == "__main__":
    words = []
    with open(WORD_FILE, "r") as file:
        for line in file:
            words.append(line.strip().upper()) #il .strip() rimuove gli spazi bianchi e "pulisce" quindi la parola
    
    #scelgo una parola a caso in words
    random_seed = randint(0, len(words)-1) #randint genera a caso tra due estremi inclusi
    word_to_guess = words[random_seed]

    n_attempts = 0
    words_tried = []
    win = False

    print_game(words_tried, word_to_guess)

    while n_attempts < 6 and not win:
        guess = input("Indovina: ").upper()
        if check_win(guess, word_to_guess):
            win = True
            print()
            print(f"COMPLIMENTI! HAI VINTO! :)")

        if(check_guess_validity(guess, words)):
            words_tried.append(guess)
            n_attempts += 1
            
        print_game(words_tried, word_to_guess)

    if(not win):
        print()
        print(f"Mi dispiace, hai perso :( La parola da indovinare era {word_to_guess}")


