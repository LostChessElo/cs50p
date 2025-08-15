def main():
    while True:
        fraction = input('Fraction: ')
      
        try:
            percentage = convert(fraction)
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split('/')
        if '.' in x or '.' in y:
            raise ValueError
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y < 0 or x > y:
            raise ValueError

        return round((x / y) * 100)

    except (ValueError, ZeroDivisionError):
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
