#thought this was a cool alternative solution to the bank problem
def bank():
    total=0 
    while True:
        user_greeting= input('Greeting: ').lower().strip()
        if 'hello' in user_greeting:
            print('$0')
            break
        elif user_greeting.startswith('h'):
            print('$20')
            total+=20
        else:
            print('$100')
            total+=100
    return f'You owe ${total} :)'
print(bank())