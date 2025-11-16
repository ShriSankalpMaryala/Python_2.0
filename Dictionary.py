dictionary = {}

while True:
    print("MINI DICTIONARY APP")
    print("1. add/update a word")
    print("2. retrieve a word's definition")
    print("3. delete a word")
    print("4. view all words")
    print("5. exit the game")

    choice = int(input("choose an option from 1-5 "))

    if choice == 1:
        word = input("enter the word ")
        definition = input("enter the definition of the word ")
        dictionary[word]= definition
        print("the word has been added")
    
    elif choice == 2:
        word = input("enter the word to retrieve ")
        if word in dictionary:
            print("{}: {}".format(word, dictionary[word]))
        else:
            print("word is not found")

    elif choice == 3:
        word = input("which word would you like to delete ")
        if word in dictionary:
            del dictionary[word]
            print("the word has been deleted")
        else:
            print("the word is not in the dictionary")
    
    elif choice == 4:
        if dictionary:
            print("words in the dictionary are- ")
            for word in dictionary:
                  print("{}: {}".format(word, dictionary[word]))
        else:
            print("dictionary is empty")
    
    elif choice == 5:
        print("exiting the game")
        break
    else:
        print("invalid choice plese enter numbers between 1-5")
                

