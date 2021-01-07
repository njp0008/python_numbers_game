# number game

favorite_number = 333
your_num = ""
num_guess = 0
max_guesses = 3
chances_left = False
print ("Pick a number between 0 and 400. The game will continue to ask you to input a number until you guess correctly. You only have 3 guesses!")

while your_num != favorite_number and not(chances_left):
    if num_guess < max_guesses:
        your_num = int(input("What is the secret number? Take a guess: "))
        num_guess +=1
    else:
        chances_left = True

if chances_left:
    print("Sorry, you've run out of guesses!")
else:
    print("You win!!")




        






