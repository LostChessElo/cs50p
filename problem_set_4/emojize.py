import emoji

def emojize():
    text=emoji.emojize(input('Input: ').lower(), language='alias')
    return f'Output: {text}'

print(emojize())

