def bank():
    user_greeting= input('Greeting: ').lower().strip()
    if 'hello' in user_greeting:
        return '$0'
    elif user_greeting.startswith('h'):
        return '$20'
    else:
        return '$100'
print(bank())



