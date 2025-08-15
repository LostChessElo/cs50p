def bank():
    user_greeting= input('Greeting: ').strip()
    print(f'${value(user_greeting)}')

def value(greeting):
    greeting = greeting.lower()
    if 'hello' in greeting:
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100

if __name__ == '__main__':
    bank()
