def twttr():
    user_str= input('Input: ').strip()
    new_str=[]
    vowels='aeiouAEIOU'
    
    for char in user_str:
        if char == ' ':
            new_str.append(char)
        elif char not in vowels:
            new_str.append(char)

    return f' Output: {''.join(new_str)}'

if __name__ == '__main__':
    print(twttr())