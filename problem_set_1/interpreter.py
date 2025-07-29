  
def math():
    user_expression = input('Expression: ').strip()
    operation = ['+', '-', '*', 'x', '/']

    user_expression = user_expression.replace('x', '*')
    user_expression = user_expression.replace(' ', '')  

    for i in range(1, len(user_expression)):
        if user_expression[i] in operation:
            operator = user_expression[i]
            x_str = user_expression[:i]
            y_str = user_expression[i+1:]
            break
    else:
        return 'Invalid'

    try:
        x = float(x_str)
        y = float(y_str)
    except ValueError:
        return 'Error'

    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y if y != 0 else 'Error'
    else:
        return 'Invalid'

print(math())


    
