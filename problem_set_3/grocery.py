def grocery():
    list=[]
    try:
        while True:
            grocery=input('').upper()
            list.append(grocery)
    except EOFError:
        count= dict.fromkeys(list, 0)
        counted=dict(sorted(count.items()))
        new_str=[]
        for i in list:
            counted[i] += 1
        for key, value in counted.items():
            new_str.append(f'{value} {key}')
        output_str='\n'.join(new_str)
    return output_str

if __name__ == '__main__':
    output_str=grocery()
    print()
    print(output_str)





