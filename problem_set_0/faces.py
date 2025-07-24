def faces():
    user_input=input('')
    if ':)' or ':(' in user_input:
        new_string= user_input.replace(':)', '🙂').replace(':(', '🙁')
    return new_string
print(faces())



