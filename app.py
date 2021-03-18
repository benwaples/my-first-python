secret_number = 3
guesses = 0

while guesses < 3:
    user_guess = int(input('make a guess'))
    if user_guess == secret_number:
        print('you got it!')
        break
    if user_guess != secret_number and guesses == 2:
        print('you lose')
    guesses = guesses + 1
print('game over')