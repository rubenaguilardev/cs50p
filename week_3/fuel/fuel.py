def main():

    def fuel():
        while True:
            try:
                x, y = input("Fraction: ").split('/')
                x = int(x)
                y = int(y)
                if x < y and x >= 0 or x == y:
                    percentage = round((x / y) * 100)
                    return "E" if percentage <= 1 else "F" if percentage >= 99 else f"{percentage}%"
            except (ValueError, ZeroDivisionError):
                pass

    print(fuel())

main()


