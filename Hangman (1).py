#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
words=["jazz","quail","example","word","antidisestablishmentarianism","pneumonoultramicroscopicsilicovolcanoconiosis",      "apple","python","montana","pennsylvania","random","end"] #supposedly, jazz is the least guessed word in hangman
        
play = "y"
while True:
    print("Let's play hangman!  Guess letters in a hidden word one at a time.  5 wrong guesses and you lose!")
    while play == "y" or play == "yes" or play == "Yes" or play == "YES":
        word = words[random.randint(0,11)]#11
        #print(word)
        blanks=[]
        for i in word:
            blanks.append("_")
        #print(blanks)
        wordblank = " ".join(blanks)
        #print(wordblank)
        wordlist=blanks[:]
        wrong = 0
        check = []
        while wrong < 5:
            print("\n"+wordblank)
            guess = input("Guess a letter! (type 'quit' to quit)(type 'check' to see what you've guessed already)\n")
            if guess == "quit" or guess == "QUIT" or guess == "Quit":
                break
            for j in range(len(blanks)):
                if guess in word:
                    if guess == word[j]:
                        blanks[j] = guess
            if guess not in word and guess != "check" and guess != "CHECK" and guess != "Check":
                print("\n"+guess,"is incorrect.")
                wrong += 1
            wordblank = " ".join(blanks)
            if "_" not in wordblank:
                print("\n"+wordblank)
                print("Congrats!  You won!")
                break
            if guess != "check" and guess != "CHECK" and guess != "Check":
                check.append(guess)
            if guess == "check" or guess == "CHECK" or guess == "Check":
                print("\nHere are the letters you've guessed:")
                print(check)
        if wrong == 5:
            print("You lost!")
            print("The word was:",word)
        if guess == "quit" or guess == "QUIT" or guess == "Quit":
            play = "n"
            break
        play = input("Want to play again? (y/n)\n")
    if play != "y" and play != "yes" and play != "Yes" and play != "YES":
        break
        


# In[ ]:





# In[ ]:




