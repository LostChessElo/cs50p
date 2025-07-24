def indoor_voice():
    s=input('enter string ')
    if s.isupper():
        return s.lower()
    else:
        return s
print(indoor_voice())
