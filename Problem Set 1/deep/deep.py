def main():
    string = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    print(check_deep(string))


def check_deep(string):
    string = string.strip().lower()
    if((string == '42') or (string == 'forty-two') or (string == 'forty two')):
        return('Yes')
    else:
        return('No')

main()