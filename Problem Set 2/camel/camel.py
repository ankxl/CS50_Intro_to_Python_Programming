def main():
    string = input('camelCase: ')
    formatted_string = transform(string)
    print(f'snake_case: {formatted_string}')

def transform(string):
    formatted_string = string
    count = 0
    for i in range(len(string)):
        if check_case(string[i]):
            formatted_string = formatted_string[0:i+count] + '_' + string[i:].lower()
            count = count + 1
    return(formatted_string)

def check_case(ch):
    return ch.isupper()

main()
