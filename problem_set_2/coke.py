def coke():
    amount=0
    change=0
    valid_coin=[5,10,25,50,100]
    while amount < 50:

        try:
            coin=int(input('Insert coin: '))
            if coin in valid_coin:
                amount += coin
                amount_due = 50-amount
            else:
                amount_due= 50 - amount
                print(f'Amount Due: {amount_due}')
                continue

            if amount_due < 0:
                change+= -1*amount_due
                print(f'Change Owed: {change}')
                break
            elif amount_due == 0:
                break
            else:
                print(f'Amount due: {amount_due}')
                continue

        except ValueError:
            print('Error')
            continue
        
    print(f'Change Owed: {change}')

if __name__ == '__main__':
    coke()



