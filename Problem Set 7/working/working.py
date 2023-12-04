import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d{1,2}):?(\d{1,2})? ([AP]M) to (\d{1,2}):?(\d{1,2})? ([AP]M)",s):
        hrs_b = int(matches.group(1))
        min_b = matches.group(2)
        meridiem_b = matches.group(3)
        hrs_e = int(matches.group(4))
        min_e = matches.group(5)
        meridiem_e = matches.group(6)

        if not (check_hours(hrs_b) and check_hours(hrs_e)):
            raise ValueError

        if min_b != None:
            if not check_minutes(int(min_b)):
                raise ValueError
            else:
                min_b = int(min_b)
        else:
            min_b = 0

        if min_e != None:
            if not check_minutes(int(min_e)):
                raise ValueError
            else:
                min_e = int(min_e)
        else:
            min_e = 0

        return time_conversion(hrs_b,min_b,matches.group(3),hrs_e,min_e,matches.group(6))

    else:
        raise ValueError

def time_conversion(hr1,mn1,md1,hr2,mn2,md2):
    if md1 == "PM":
        if hr1 != 12:
            hr1 = hr1 + 12
    else:
        if hr1 == 12:
            hr1 = 0
    if md2 == "PM":
        if hr2 != 12:
            hr2 = hr2 + 12
    else:
        if hr2 == 12:
            hr2 = 0
    return(f"{hr1:02}:{mn1:02} to {hr2:02}:{mn2:02}")

def check_hours(hrs):
    return (0 <= hrs <= 12)

def check_minutes(min):
    return (0 <= min < 60)

if __name__ == "__main__":
    main()
