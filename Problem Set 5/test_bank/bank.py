def main():
    string = input('Greeting: ')
    print('$'+ str(value(string)))


def value(greeting):
    string = greeting.strip().lower()

    if string.startswith('hello'):
        return 0
    elif string.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
