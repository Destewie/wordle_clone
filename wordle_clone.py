from random import randint
import os

WORD_FILE = "parole_5_lettere.txt"
#GREEN = "\033[32m"
#YELLOW = "\033[33m"

def highlight_text(text, color_code):
    return f"{color_code}{text}\033[0m"


def check_win(guess, correct_word):
    return guess == correct_word


def check_guess_validity(guess, all_words):
    return len(guess) == 5 and guess in all_words



def print_game(words_tried, correct_word):
    os.system("clear")

    print("BENVENUTO NEL CLONE BRUTTO DI WORDLE FATTO DAL FEDE_DES :)")
    print(f"La parola da indovinare ha {len(word_to_guess)} lettere")
    print("Hai 6 tentativi per indovinare la parola")
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

    while n_attempts < 6:
        guess = input("Indovina: ").upper()
        if check_win(guess, word_to_guess):
            print()
            print(f"COMPLIMENTI! HAI VINTO! :)")

        if(check_guess_validity(guess, words)):
            words_tried.append(guess)



            n_attempts += 1




