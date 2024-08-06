import random

def hangman():
    
    list =['coder','programmer','gamer','boxer','volleyball','gossip','cricket','icebox','vampire']
    
    word = random.choice(list)
    word_length = len(word)
    guessed_letters = []
    wrong_guesses = 0
    total_attempts = 8

    print("Welcome to Hangman game!")

    display = "_" * word_length

    while wrong_guesses < total_attempts and "_" in display:
        print(display)
        print("wrong Guesses:", wrong_guesses)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.  Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("This letter is already guessed.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            new_display = ""
            for i in range(word_length):
                if word[i] == guess:
                    new_display += guess
                else:
                    new_display += display[i]
            display = new_display
        else:
            wrong_guesses += 1
            print("wrong guess!")

    if "_" not in display:
        print(f"Congratulations! YOU WIN. The word was {word}")
    else:
        print(f"Game over! YOU LOSE. The word was {word}")

if __name__ == "__main__":
    hangman()
