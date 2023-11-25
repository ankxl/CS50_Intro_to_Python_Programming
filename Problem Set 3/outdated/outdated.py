month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    get_input('Date: ')

def get_input(prompt):
    while True:
        try:
            string = input(prompt)
            if len(string.split('/')) == 3:
                month, date, year = string.split('/')
                month = int(month)
                date = int(date)
                year = int(year)
                if check_date_month(date,month):
                    print(f'{year}-{month:02}-{date:02}')
                    break
            else:
                string, year = string.split(',')
                month, date = string.split(' ')
                year = int(year)
                date = int(date)
                month = month_list.index(month) + 1
                if check_date_month(date,month):
                    print(f'{year}-{month:02}-{date:02}')
                    break
        except ValueError:
            pass

def check_date_month(date,month):
    if month > 12 or month <= 0:
        return False
    if (month in [1,3,5,7,8,10,12] and (date > 31 or date <= 0)):
        return False
    if (month in [4,6,9,11] and (date > 30 or date <= 0)):
        return False
    if month == 2 and (date > 29 or date <= 0):
        return False
    return True

main()