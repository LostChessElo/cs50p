import sys


def main():
    file_ = args()
    print(count(file_))


def args():
    if len(sys.argv) != 2:
        sys.exit('Too few command-line arguments' if len(sys.argv) < 2
                 else 'Too many command-line arguments')
    if sys.argv[1].endswith('.py'):
        return sys.argv[1]
    else:
        sys.exit('Not a Python file')


def check_line(s):
    if s.startswith('#') or len(s) == 0:
        return False
    else:
        return True


def count(f):
    try:
        count_lines = 0
        with open(f, 'r') as file:
            for line in file:
                if check_line(line.strip()):
                    count_lines += 1
            return count_lines

    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__ == '__main__':
    main()
