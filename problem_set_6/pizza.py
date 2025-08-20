import sys
import csv
from tabulate import tabulate


def main():
    try:
        file_ = args()
        headers = get_header(file_)
        table = []  # empty 2d array
        with open(file_) as file:
            for line in file:
                if line.rstrip() not in headers:
                    item, small, large = line.rstrip().split(',')
                    table.append([item, small, large])

            print(tabulate(table, headers.split(','), tablefmt="grid"))

    except FileNotFoundError:
        sys.exit('File does not exist')

#check command-line arguments
def args():
    if len(sys.argv) != 2:
        sys.exit('Too few command-line arguments' if len(sys.argv) < 2 else 'Too many command-line arguments')
    if sys.argv[1].endswith('.csv'):
        return sys.argv[1]
    else:
        sys.exit('Not a CSV file')


def get_header(f):
    try:
        with open(f, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = ','.join(next(reader))
            return header
    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__ == '__main__':
    main()

