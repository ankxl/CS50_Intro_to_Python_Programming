import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if(len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")

    if (not sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")

    count = get_file(sys.argv[1])
    print(count)

def get_file(name):
    try:
        with open(name,"r") as file:
            lines = file.readlines()
            return (get_count(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")

def get_count(lines):
    count = 0
    for line in lines:
        if line.strip().startswith("#") :
            continue
        elif line.strip() in ("",None," "):
            continue
        else:
            count += 1
    return count


if __name__ == "__main__":
    main()
