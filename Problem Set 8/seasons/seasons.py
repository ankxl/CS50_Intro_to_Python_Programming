from datetime import date
import re
import sys
import inflect


def main():
    day_dob = get_date()
    day_today = date.today()
    day_dif = day_today - day_dob
    minutes = Day_to_Minutes.get(day_dif.days)
    print(f"{minutes} minutes")


class Day_to_Minutes():
    def __init__(self,minutes):
        self.mins = minutes
        # print(f"__init: {self.mins}")

    @classmethod
    def get(cls,days):
        # print(f"get function {days}")
        return(cls(days*24*60))

    def __str__(self):
        eng = inflect.engine()
        return(eng.number_to_words(self.mins,andword="").capitalize())



def get_date():
    date_input = input("Date of Birth: ")
    (year,month,day) = validate_date(date_input)
    return(date(year,month,day))

def validate_date(date_input):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$",date_input):
        return(int(match.group(1)),int(match.group(2)),int(match.group(3)))
    else:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()
