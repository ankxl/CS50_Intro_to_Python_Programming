def main():
    string = input("Fraction: ")
    print(gauge(convert(string)))


def convert(fraction):
    x,y = fraction.split('/')
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return(round(x * 100 / y))


def gauge(percentage):
    if percentage <= 1:
        return('E')
    elif percentage >= 99 and percentage <=100:
        return('F')
    elif percentage < 100:
        return(f'{percentage}%')


if __name__ == "__main__":
    main()
