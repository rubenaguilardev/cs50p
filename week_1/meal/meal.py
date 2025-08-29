def main():
    time = input('What time is it? ')
    meal_time = convert(time)

    if 7.0 <= meal_time <= 8.0:
        print('breakfast time')
    elif 12.0 <= meal_time <= 13.0:
        print('lunch time')
    elif 18.0 <= meal_time <= 19.0:
        print('dinner time')


def convert(time):
    hour, minutes = time.split(':')
    hour = int(hour)
    minutes = int(minutes) / 60
    return hour + minutes


if __name__ == "__main__":
    main()