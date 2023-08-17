def main():
    string = input()
    print(convert(string))

def convert(string):
    return(string.replace(':)','\U0001F642').replace(':(','\U0001F641'))

main()