def outdated():
    months= {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        date = input('Date: ').title().strip()
        #8/8/2008 = [8, 8, 2008]
        if '/' in date:
            date=date.split('/')
            if len(date[0]) > 2 or len(date[1]) > 2:
                continue
            try:
                year= int(date[-1])
                month= int(date[0])
                day= int(date[1])
                if month > 12 or day > 31:
                    continue
            except ValueError:
                continue

            if len(str(month)) < 2 and len(str(day)) < 2:
                return f'{year}-{month:02d}-{day:02d}' #2008-08-08
            elif len(str(day)) < 2 and len(str(month)) > 1:
                 return f'{year}-{month}-{day:02d}'#2008-11-08
            elif len(str(day)) > 1 and len(str(month)) < 2:
                 return f'{year}-{month:02d}-{day}' #2008-08-11
            else:
                return f'{year}-{month}-{day}' #2008-11-12
        else:
            # september 8 2008 = [September, 8, 2008]
            if ',' in date:
                date=date.replace(',',' ')
                date=date.split()
                if date[0] in months:
                    try:
                        month=months[date[0]]
                        day=int(date[1])
                        year=date[-1]
                        if day > 31:
                            continue
                    except ValueError:
                        continue

                    if len(str(month)) < 2 and len(str(day)) < 2:
                        return f'{year}-{month:02d}-{day:02d}' #2008-08-08
                    elif len(str(day)) < 2 and len(str(month)) > 1:
                        return f'{year}-{month}-{day:02d}'#2008-11-08
                    elif len(str(day)) > 1 and len(str(month)) < 2:
                        return f'{year}-{month:02d}-{day}' #2008-08-11
                else:
                    continue

            else:
                continue
            
if __name__ == '__main__':
    print(outdated())
