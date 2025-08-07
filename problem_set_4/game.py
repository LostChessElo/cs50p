import random

def main():
    while True:
        try:
            level= int(input('Level: '))
            break
        except ValueError:
            continue

    comp_guess=random.randint(1,level)

    while True:
        try:
            guess=int(input('Guess: '))
        except ValueError:
            continue
        if guess > 0:
            if guess > comp_guess:
                print('Too Large!')
                continue
            elif guess < comp_guess:
                print('Too small!')
                continue
            elif guess == comp_guess:
                print('Just right!')
                break
        else:
            continue
        

main()