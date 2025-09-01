def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_letters(s[0:2]):
        if min_max_length(s):
            if middle_characters(s):
                return only_alnum(s)



def start_letters(firstTwoLetters):
    return True if firstTwoLetters.isalpha() else False


def min_max_length(plate):
    digits = len(plate)
    return True if digits <= 6 and digits >= 2 else False


def middle_characters(s):
    if s.isalpha():
        return True
    else:
        for character in s:
            if character.isnumeric():
                index_of = s.index(character)
                return True if character != '0' and s[index_of:].isnumeric() else False


def only_alnum(s):
    return True if s.isalnum() else False


main()
