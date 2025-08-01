def main():
    while True:
        fraction = input('Fraction: ')

        # check formatting
        if '/' in fraction:
            fraction = fraction.split('/')
        else:
            continue

        # check for decimals
        if '.' in fraction[0] or '.' in fraction[1]:
            continue

        try:
            x = int(fraction[0])
            y = int(fraction[-1])
        except ValueError:
            continue

        if x >= 0 and y > 0:
            if x <= y:
                result = (x / y) * 100
                fuel = round(result)
                if fuel <= 1:
                    return 'E'
                elif fuel >= 99:
                    return 'F'
                else:
                    return f'{fuel}%'
            else:
                continue
        else:
            continue

if __name__ == '__main__':
    print(main())
