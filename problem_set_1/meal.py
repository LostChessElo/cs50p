def main():
   time= convert(input('What  time is it? ').strip())

   if 7.0 <= time <= 8.0:
       return 'breakfast time'
   elif 12.0 <= time <= 13.00:
       return 'lunch time'
   elif 18.0 <= time <= 19.0:
       return 'dinner time'
   else:
       return ''

def convert(time):
    time = time.split(':')

    try:
        hours= float(time[0])
        minutes= (float(time[1])) / 60
    except ValueError:
        return 'Invalid time input'

    return hours + minutes


if __name__ == '__main__':
    print(main())
