from pyfiglet import Figlet, FontNotFound
import argparse

def fig():
    parser= argparse.ArgumentParser()
    parser.add_argument('-f','--font', default= 'standard', help='font to use')
    args=parser.parse_args()

    try:
        fig=Figlet(font=args.font, justify="centre")
        text= fig.renderText(input('Input: '))
        return f'Output:\n{text}'
    except FontNotFound:
        return 'font not found'
    except Exception as e:
        return str(e)

print(fig())
