from validators import email

def main():
    email_id = input("What's your meail address? ")
    if email(email_id) == True:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
