def twttr():
    user_str = input('Input: ')
    print('Output:',shorten(user_str))


def shorten(wrd):
    vowels = 'aeiouAEIOU'
    for char in wrd:
        if char in vowels:
            wrd = wrd.replace(char, '')
    return wrd

if __name__ == '__main__':
    twttr()


