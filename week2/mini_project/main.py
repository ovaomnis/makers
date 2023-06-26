from random import randint

username = input('Please enter your username: ')
stopped = False
# Inicilizing game
while True:
    wanna_play = input(f'{username}, do you want to start game ?\n(yes/no): ')
    answers = {'yes': False, 'no': True}
    if wanna_play.lower() in answers:
        stopped = answers[wanna_play.lower()]
        break
    else:
        print('Answer have to be yes or not. Other answers will not count')
        continue
print("")
print('''Game Rules:
Guess number will generated automaticly between 1 and 99
Purpose of the game is guess this number''')
print('')

# Starting game
while not stopped:
    guess_num = randint(1, 100)
    tries = 0

    # Guessing number
    while True:
        print(num := input('Enter number between 1 and 99: '))
        if num.isnumeric():
            num = int(num)
            if num < guess_num:
                print('Your number is Lower')
                tries += 1
            elif num > guess_num:
                print('Your number is Greater')
                tries += 1
            else:
                break
        else:
            print('Ansver have to be numeric')
            continue
    
    print('')
    print(f'You guessed!, it tooked {tries} tries to guess the number')
    print('')
    
    # Requestin whether player want to continue
    while True:
        wanna_play = input(f'{username}, do you want to continue game ?\n(yes/no): ')
        answers = {'yes': False, 'no': True}
        if wanna_play.lower() in answers:
            stopped = answers[wanna_play.lower()]
            break
        else:
            print('Answer have to be yes or not. Other answers will not count')
            continue