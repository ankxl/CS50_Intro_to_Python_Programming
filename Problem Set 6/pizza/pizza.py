import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if (len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")

    if(not sys.argv[1].strip().endswith(".csv")):
        sys.exit("Not a CSV file")

    get_file(sys.argv[1])


def get_file(filename):

    try:
        with open(filename,"r") as file:
            reader = csv.reader(file)
            count = 0
            rows = []
            for type,small,large in reader:
                if reader.line_num == 1:
                    headers = [type,small,large]
                else:
                    rows.append([type,small,large])
            print(tabulate(rows,headers=headers,tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
