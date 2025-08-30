def main():

    amount_due = 50

    while amount_due >= 0: 
        print(f'Amount Due: {amount_due}')
        amount_due = amount_due - get_coin(amount_due)
        if amount_due <= 0:
            print(f'Change Owed: {amount_due * -1}')
            break
            
    
def get_coin(amount_due):
    valid_coins = [5, 10, 25]
    while True:
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            return coin
        else:
            print(f'Amount Due: {amount_due}')
        

main()