import csv
import sys


def main():
    try:
        file_r, file_w = file_args()
        data = read_file(file_r)

        with open(file_w, 'w') as csvf:
            writer = csv.DictWriter(csvf, fieldnames= ['first' , 'last', 'house'])
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        sys.exit('File does not exist')


def file_args():
    if len(sys.argv) != 3:
        sys.exit('Too few command-line arguments' if len(sys.argv) < 3
                  else 'Too many command-line arguments')
    if sys.argv[1].endswith('.csv'):
        return sys.argv[1], sys.argv[2]
    else:
        sys.exit(f'Could not read {sys.argv[1]}')


def read_file(f):
    rows = []
    with open(f) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last, first  = row['name'].split(',')
            house = row['house']
            new_dict = {'first': first.strip(), 'last': last.strip(), 'house': house}
            rows.append(new_dict)
        return rows


if __name__ == "__main__":
    main()
