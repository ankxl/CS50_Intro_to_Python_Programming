def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_incorrect_len(s):
        return False
    if not(check_alphanum_char(s)):
        return False
    if not(check_character_12(s)):
        return False
    return check_number_order(s)


def check_incorrect_len(s):
    return (len(s) < 2) or (len(s)>6)

def check_alphanum_char(s):
    return (s.isalnum())

def check_character_12(s):
    return(s[0].isalpha() and s[1].isalpha())

def check_number_order(s):
    number = False
    for i in range(len(s)):
        if s[i].isnumeric():
            if s[i] == '0' and number == False:
                return False
            number = True
        if number == True and s[i].isalpha():
            return False
    return True

if __name__ == "__main__":
    main()
