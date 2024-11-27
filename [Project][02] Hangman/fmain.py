import random
from hangman_art import stages, logo
from hangman_words import word_list

# ფუნქციის მიზანია ბანერის ჩვენება და თამაშის დაწყება;
def start_game():
    print(logo)
    print("\nკეთილი იყოს თქვენი მობრძანება Hangman-ის თამაშში!")
    print("\nთქვენ გექნებათ " + str(len(stages) - 1) + " შანსი სიტყვების გამოსაცნობად.\n")

# სიტყვების არჩევა
def choose_word():
    chosen_words = random.choice(word_list)
    return chosen_words["word"], chosen_words["quest"]

# ცარიელი ხაზის შექმნა სიტყვების გამოსაცნობად
def initialize_display(word_length):
    return ["_" for _ in range(word_length)]

# სიმბოლოს შეყვანის ფუნქცია
def get_valid_guess(valid_symbols):
    while True:
        guess = input("\nგთხოვთ, შეიყვანეთ ერთი სიმბოლო: ")
        if len(guess) != 1:
            print("\nშეიყვანეთ მხოლოდ ერთი სიმბოლო!")
        elif guess not in valid_symbols:
            print("\nშეიყვანეთ ერთი ქართული სიმბოლო!")
        else:
            return guess

# სიმბოლოს შემოწმება სიტყვაში
def update_display(chosen_word, display, guess):
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
