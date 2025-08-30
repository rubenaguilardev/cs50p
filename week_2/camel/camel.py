def main():

    var = input("camelCase: ")
    print(f"snake_case: {convertToSnakeCase(var)}")


def convertToSnakeCase(var):
    converted = ''
    for letter in var:
        if letter.isupper():
            converted += '_'
            converted += letter.lower()
        else:
            converted += letter
    return converted


main()