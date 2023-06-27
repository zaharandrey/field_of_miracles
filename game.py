import random

words = ['apple', 'banana', 'orange', 'mango']


def play_game():
    word = random.choice(words)
    attempts = int(input("Введіть кількість спроб: "))

    guessed_letters = []
    guessed_word = ['*'] * len(word)

    while attempts > 0:
        print(' '.join(guessed_word))

        guess = input("Введіть літеру або слово: ").lower()

        if guess.isalpha():
            if guess in guessed_letters:
                print("Ви вже вгадали цю літеру.")
            elif guess in word:
                guessed_letters.append(guess)
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess
            else:
                print("Такої літери немає.")
                attempts -= 1
        else:
            if guess == word:
                print("Вітаємо, ви вгадали слово!")
                return
            else:
                print("Слово не правильне.")
                attempts -= 1

        if '*' not in guessed_word:
            print("Вітаємо, ви вгадали слово!")
            return

    print("Ви програли. Спроби закінчилися. Загадане слово:", word)


play_game()
