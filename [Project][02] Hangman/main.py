from hangman_art import stages
from hangman_words import valid_simbols
from fmain import (
    start_game,
    choose_word,
    initialize_display,
    get_valid_guess,
    update_display,
)

def play_game():
    """
    თამაშის სრული განსაზღვრა. 
    მოთამაშეს შეუძლია ან ასო გამოიცნოს, ან მთელი სიტყვა სცადოს.
    თუ სიტყვით სცადა და არასწორია, თამაში დასრულდება.
    """
    start_game()

    # შემთხვევითი სიტყვის არჩევა და მისი აღწერა
    chosen_word, quest = choose_word()
    word_length = len(chosen_word)
    print("\n" + quest + "\n")
    display = initialize_display(word_length)

    lives = len(stages) - 1
    game_is_finished = False

    while not game_is_finished:
        print(f"\n{' '.join(display)}")  # ეკრანზე სიტყვა _(ქვედახაზი)-ებით
        print(f"\nშენ დაგრჩა {lives} ცდა!")

        # მომხმარებლის არჩევანი: ასო ან სიტყვა
        print("1. სცადე ასო-ასო")
        print("2. გარისკე სიტყვა, მაგრამ გაითვალისწინე - თუ შეცდი, წააგებ.")
        user_choice = input("\nრას ირჩევ '1' თუ '2' ?   - ")
        if user_choice == '1':
            guess = get_valid_guess(valid_simbols)

            if guess in display:
                print(f"\nშენ უკვე გამოიცანი ეს სიმბოლო - {guess}")
            else:
                update_display(chosen_word, display, guess)

            if guess not in chosen_word:
                lives -= 1
                if lives == 0:
                    game_is_finished = True
                    print("\nწააგე!")
                    print("\nსიტყვა იყო:", chosen_word)
                    print("\nთამაში დასრულდა!")
                elif lives == 1:
                    print(f"\n {guess}, არ არის სიტყვაში. ბ ო ლ ო   ც დ ა!")
                else:
                    print(f"\n {guess}, სხვაგან ხარ, {lives} ცდა გაქვს ;).")
        elif user_choice == '2':
            word_guess = input("\nშეიყვანე მთელი სიტყვა: ").lower()
            if word_guess == chosen_word:
                game_is_finished = True
                print(f"\n{chosen_word}")
                print("\nგილოცავ, შენ სწორად გამოიცანი მთელი სიტყვა!\n")
            else:
                game_is_finished = True
                print("\nარასწორი სიტყვაა! თამაში დასრულდა.")
                print("\nსიტყვა იყო:", chosen_word)
        else:
            print("\nარასწორი არჩევანი. სცადე თავიდან.")

        # ეკრანზე დარჩენილი ცხოვრების საფეხურები
        print(stages[lives])

        # გამარჯვების შემოწმება
        if "_" not in display and not game_is_finished:
            game_is_finished = True
            print(f"\n{' '.join(display)}")
            print("\nგილოცავ, შენ შეძელი ეს!\n")

# თამაშის გაშვება
if __name__ == "__main__":
    while True:
        play_game()
        restart = input("\nგსურს თამაში თავიდან? (დიახ/არა/ok/no): ").lower()
        if restart != 'დიახ' or restart != 'ok':
            print("\nმადლობა თამაშისთვის! ნახვამდის!")
            break
