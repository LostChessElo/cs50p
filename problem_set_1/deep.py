def answer():
    correct=['42' , 'forty-two', 'forty two' ]
    user_answer=input('What is the answer to the Great Question of Life, the Universe and Everything? ').lower().strip()
    if user_answer in correct:
        return 'Yes'
    else:
        return 'No'
print(answer())

