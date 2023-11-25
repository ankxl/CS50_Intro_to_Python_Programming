def main():
    result = get_input('Fraction: ')
    if result <= 1:
        print('E')
    elif result >= 99 and result <=100:
        print('F')
    elif result < 100:
        print(f'{result}%')
    else:
        main()

def get_input(prompt):
    while True:
        try:
            string = input(prompt)
            x,y = string.split('/')
            x = int(x)
            y = int(y)
            result = round(x * 100 / y)

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return result

main()