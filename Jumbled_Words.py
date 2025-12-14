import random
words = ["orange","banana","bus","apple","juice","dictionary","function","block","generator","movie"]

def jumble_word(word):
    words = list(word)
    random.shuffle(words)
    return "".join(words)

def get_hint(word):
    return "the first letter of the word is  {}".format(word[0].upper())

def play_game():
    score = 0
    rounds = 5
    print("Hi, welcome to the Jumble Word Game")
    for round in range(1,rounds+1):
        word = random.choice(words)
        scrambled_word = jumble_word(word)

        print("Round {}:".format(round))
        print("This is the the scrambled word {}".format(scrambled_word))
        
        hint = (input("Do you want a hint yes or no? ").lower() )
        if hint == "yes":
            print(get_hint(word))

        guess = input("Guess the original word: ").lower()

        while not guess.isalpha():
            print("Please enter a valid word ")
            guess = input("Guess the original word: ").lower()
        
        if guess == word:
            print("Congratulations you have guessed it right")
            score += 1
        else:
            print("Incorrect guess the correct word was {}".format(word))
    
    print("Game over your final score is {}/{}".format(score,rounds))

play_game()

