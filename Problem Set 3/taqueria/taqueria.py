def main():

    total = 0
    while True:
        value = get_input('Item: ')
        if value == 0:
            continue
        elif value != None:
            total = total + value
            print(f'Total: ${total:.2f}')
        else:
            break

def get_input(prompt):

    items ={
            "baja taco": 4.00,
            "burrito": 7.50,
            "bowl": 8.50,
            "nachos": 11.00,
            "quesadilla": 8.50,
            "super burrito": 8.50,
            "super quesadilla": 9.50,
            "taco": 3.00,
            "tortilla salad": 8.00
        }
    try:
        key = input(prompt).lower()
        return items[key]
    except KeyError:
        return 0
    except EOFError:
        return None


main()


