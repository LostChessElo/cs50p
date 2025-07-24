def einstein():
    m=input('what is the mass? ')
    if m.isdigit():
        m=int(m)
    else:
        return 'mass mustt be a number'
    result= m*((300000000)**2)
    return f'E= {result} Joules'
print(einstein())
