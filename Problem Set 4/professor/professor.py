import random


def main():
    level = get_level()
    score = 0
    for i in range(0,10):
        x,y = generate_integer(level)
        res = -1
        wr = 0
        for j in range(0,3):
            try:
                res = int(input(f"{x} + {y} = "))
                if res == (x+y):
                    score = score + 1
                    break
                print("EEE")
                wr = wr + 1
            except ValueError:
                print("EEE")
                wr = wr + 1
        if wr == 3:
            print(f"{x} + {y} = {(x+y)}")
    print(f"Score: {score}")


def get_level():
    prompt = "Level: "
    while True:
        try:
            num = int(input(prompt))
            if 1<= num <=3:
                return num
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    x = 0
    y = 0

    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return(x,y)


if __name__ == "__main__":
    main()
