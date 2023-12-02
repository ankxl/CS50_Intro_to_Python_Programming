import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].strip().endswith(".csv"):
        sys.exit("Not a CSV file")

    get_file(sys.argv[1],sys.argv[2])

def get_file(readfile,writefile):
    try:
        with open(readfile) as file:
            reader = csv.DictReader(file)
            fwrite = open(writefile,"w")
            writer = csv.DictWriter(fwrite,fieldnames=['first','last','house'])
            writer.writeheader()
            for row in reader:
                last, first = row['name'].split(', ')
                writer.writerow({'first':first,'last':last,'house':row['house']})
            fwrite.close()
    except FileNotFoundError:
        sys.exit(f"Could not read {readfile}")



if __name__ == "__main__":
    main()
