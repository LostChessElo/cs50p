import inflect

def adieu():
    names=[]
    p=inflect.engine()
    
    try:
        while True:
            name= input('Name: ').title()
            if name.isalpha():
                names.append(name)
    except EOFError:
        return f'\nAdieu, adieu, to {p.join(names)}'

if __name__ == '__main__':
    print(adieu())
