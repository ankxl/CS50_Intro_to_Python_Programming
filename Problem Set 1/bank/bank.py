def main():
    string = input('Greeting: ')
    print('$'+ str(bank_output(string)))

def bank_output(string):
    string = string.strip().lower()

    if string.startswith('hello'):
        return 0
    elif string.startswith('h'):
        return 20
    else:
        return 100


main()