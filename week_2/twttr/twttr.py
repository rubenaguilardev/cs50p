def main():
    text = input('Input: ')
    print(f"{remove_vowels(text)}")


def remove_vowels(word):
    vowels = 'aAeEiIoOuU'
    extracted = ''

    for letter in word:
        if letter not in vowels:
            extracted += letter
    return extracted

main()