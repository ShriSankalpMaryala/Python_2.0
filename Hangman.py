import random
def hangman():
    words = ["maryland","typewriter","computer","dictionary","generator","territory","pencil","theatre","questions","storage" ]
    word = random.choice(words)
    guessed_word = ["_"]*len(word)
    max_attempts = 6
    attempts = 0
    guessed_letters = []
    print("Guess the word one letter at a time")
    print("Word: ","".join(guessed_word))

    while attempts < max_attempts and "_" in guessed_word:
        guess = input("enter a letter ").lower()

        #checking if it is a valid input
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter")
            continue
        # check if letter is guessed already
        if guess in guessed_letters:
            print("You already guessed that letter try again")
            continue

        guessed_letters.append(guess)

        # check if the guess is correct
        if guess in word:
            print("Good guess")
            for i in range(len(word)):
                if word[i]== guess:
                    guessed_word[i]= guess
        else:
            attempts += 1 
            print("Wrong guess you have {}attempts left".format(max_attempts - attempts))
        
        print("Word: ","".join(guessed_word))
    
    if "_" not in guessed_word: #
        print ("Congratulations! You guessed the word '{}'.".format(word))
    else:
        print ("Game Over! The word was '{}'. Better luck next time!".format(word))

hangman()
