def main():
    
    fuel_amount = get_fuel_amount()
    check_percentage(fuel_amount)


def get_fuel_amount():

    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x, y = int(x), int(y)
            if x > y or x < 0 or y < 0:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return x / y * 100
        

def check_percentage(fuel):
      
    if fuel <= 1:
        print('E')
    elif fuel >= 99:
        print('F')
    else:
        print(f"{round(fuel)}%")
        


main()

