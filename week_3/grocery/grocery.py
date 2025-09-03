def main():

    get_items()


def get_items():

    list_of_items = {}

    while True:
        try:
            item = input("")
        except EOFError:
            print("")
            sorted_items = dict(sorted(list_of_items.items()))
            for item in sorted_items:
                print(f"{list_of_items[item]} {item.upper()}")
            break

        if item not in list_of_items:
            list_of_items[item] = 1
        else:
            list_of_items[item] += 1


main()
