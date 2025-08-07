import random

def main():
    score=0
    tries=0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        while tries < 3:
            try:
                ans=int(input(f'{x} + {y} = '))
                if ans == x + y:
                    tries = 0
                    score += 1
                    break
                else:
                    print('EEE')
                    tries += 1
            except ValueError:
                print('EEE')
                tries += 1
        if tries == 3:
            tries = 0
            print(f'{x} + {y} = {x + y}')
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            level= int(input('Level: '))
            if 1 <= level <=3:
                return level
            else:
                raise ValueError
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
