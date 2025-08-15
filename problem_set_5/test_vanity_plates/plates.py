
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters=[]
    numbers=[]

    #bool value to check if a number occurs at the end of a string
    number=False
    if s[0].isalpha() and 2 <= len(s) <=6 and s.isupper():

        #check string forrmat i.e ABC123
        for char in s:
            if char.isdigit():
                number=True
                numbers.append(char)
            elif char.isalpha():
                if number:
                    return False
                letters.append(char)
            else:
                return False
        if len(letters) >= 2:
            if numbers:
                if numbers[0] =='0':
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
