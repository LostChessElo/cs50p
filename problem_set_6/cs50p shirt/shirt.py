import sys
import os
from PIL import Image, ImageOps


def main():
    person = shirt()


def file_args():
    ext = ['.png', '.jpeg', '.jpg']

    if len(sys.argv) != 3:
        sys.exit('Too few command-line arguments' if len(sys.argv) < 3
                 else 'Too many command-line arguments')

    input_f = sys.argv[1]
    output_f = sys.argv[2]

    inpt_ext = os.path.splitext(input_f)[1].lower()  # '.png'
    outpt_ext = os.path.splitext(output_f)[1].lower()

    if inpt_ext in ext and outpt_ext in ext:
        if inpt_ext == outpt_ext:
            return input_f, output_f
        else:
            sys.exit('Input and output have different extensions')
    else:
        sys.exit('Invalid Input')


def shirt():
    input_f, output_f = file_args()

    try:
        student = Image.open(input_f)
        image = Image.open('shirt.png')
    except FileNotFoundError:
        sys.exit(f'Cant open {input_f}')

    size = image.size
    person = ImageOps.fit(student, size)
    person.paste(image, image)
    person.save(output_f)
    return person


if __name__ == "__main__":
    main()
