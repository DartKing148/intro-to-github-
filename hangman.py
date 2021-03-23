import random

print("H A N G M A N")
while True:
    print()
    user_game = input('Type "play" to play the game, "exit" to quit: ')
    if user_game == "exit":
        exit()
    elif user_game != "play":
        continue

    words = ['python', 'java', 'kotlin', 'javascript', 'gachi', 'mother', 'father', 'assembler', 'putin', 'killer', 'murder']
    word = random.choice(words)
    secret = len(word) * '-'
    list_user_letter = []
    user_answers = ""
    lives = 8

    while True:
        print()
        print(secret)

        user_letter = input("Input a letter: ")
        list_user_letter.append(user_letter)
        answer = []
        if len(user_letter) != 1:
            print("You should input a single letter")
            continue

        elif not user_letter.islower():
            print("Please enter a lowercase English letter")
            continue

        elif user_letter in user_answers:
            print("You've already guessed this letter")

        elif user_letter not in word:
            print("That letter doesn't appear in the word")
            lives -= 1

        if len(user_letter) == 1:
            user_answers += user_letter

        for letter in word:
            if letter in list_user_letter:
                answer.append(letter)
            else:
                answer.append("-")

        secret = ("".join(answer))

        if lives == 0:
            print("You lost!")
            break

        if secret == word:
            print("""You guessed the word!
You survived!""")
            break
