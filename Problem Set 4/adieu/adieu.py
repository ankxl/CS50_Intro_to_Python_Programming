def main():
    names = get_input("Name: ")
    initial = "Adieu, adieu, to"
    output = format_string(initial,names)
    print("")
    print(output)


def get_input(prompt):
    names=[]
    while True:
        try:
            name = input(prompt)
            names.append(name)
        except EOFError:
            return names

def format_string(initial, names):
    length = len(names)
    if length < 1:
        sys.exit("Didnt enter any names")
    initial = initial + " " + names[0]
    if length == 1:
        return initial
    elif length == 2:
        return (initial + " and " + names[-1])

    initial = initial + ", "

    for i in range(1,length-1):
        print(i)
        initial = initial + names[i] + ", "

    return (initial + "and " + names[-1])


main()
