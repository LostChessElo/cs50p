def playback():
    user_input=input('' )
    s=user_input.split()
    for i in s:
        new_string= '...'.join(s)
    return new_string
print(playback())
