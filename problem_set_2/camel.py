def camel_case():
    snake_case=''
    for char in input('camelCase: '):
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char

    return f'snake_case: {snake_case}'

print(camel_case())
