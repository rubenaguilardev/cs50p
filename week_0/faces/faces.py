def main():
    emotion = input('')
    convert(emotion)

def convert(str):
    str = str.replace(":(", "🙁")
    str = str.replace(":)", "🙂")
    print(str)

main()
