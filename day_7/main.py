import random
from word import word_list
from art import stages,logo

help_array = []
picked_word = random.choice(word_list)

for _ in picked_word:
    help_array.append("_")
    
print(logo)
game_on = True
lives = 6
while game_on:
    user_letter = input("Guess the letter: \n").lower()
    
    for letter in range(len(picked_word)):
        if picked_word[letter] == user_letter:
            help_array[letter] = picked_word[letter]
    if user_letter not in picked_word:
        print("The letter you guess is not in the word. You lose life.")
        lives -= 1
    if user_letter in help_array:
        print("Your guess word is actually guessed. Try again.")
    print(f"{' '.join(help_array)}")
    print(stages[lives])
    
    if "_" not in help_array:
        print("You win!!")
        game_on = False
    elif lives == 0:
        print("You lose.")
        game_on = False
    





