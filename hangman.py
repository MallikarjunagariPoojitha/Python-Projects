import random
import hangman_words
from hangman_art import logo
from hangman_art import stages
print(logo)
choosen_word=random.choice(hangman_words.word_list)
print(choosen_word)
#guess_letter=input("Guess a letter").lower()
display=[]
for i in range(len(choosen_word)):
    display.append("_")
live=6
#print(display)  
end_game=False                     
while not end_game:
    guess_letter=input("Guess a letter").lower()
    if guess_letter in display:
        print(f"You already guessed {guess_letter}")
    for i in range(len(choosen_word)):
         letter=choosen_word[i]
         if guess_letter==letter:
             display[i]=guess_letter
    if guess_letter not in choosen_word:
        print(f"You guessed {guess_letter} is not in the word! You lose")
        live=live-1
        if live==0:
            end_game=True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
       end_game=True
       print("You won!")
    print(stages[live])
