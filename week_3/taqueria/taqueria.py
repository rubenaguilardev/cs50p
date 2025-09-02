def main():

    get_item()

def get_item():
    menu = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    cost = 0

    while True:

        try:
            choice = input("Item: ").lower()
            for item in menu:
                if item == choice:
                    cost += menu[item]
                    print(f"Total: ${cost:.2f}")
        except EOFError:
            print(f"\nTotal: ${cost:.2f}")
            break


main()
