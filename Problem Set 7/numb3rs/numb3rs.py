import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    print(ip)
    if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip):
        for num in matches.groups():
            num = int(num)
            if num < 0 or num > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
