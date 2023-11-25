def main():
    items ={}
    while True:
        try:
            key = input('').upper()
        except EOFError:
            keys = list(items.keys())
            keys.sort()
            print()
            for key in keys:
                print(f'{items[key]} {key}')
            break
        else:
            if items.get(key) is not None:
                items[key] = items[key] + 1
            else:
                items[key] = 1

main()