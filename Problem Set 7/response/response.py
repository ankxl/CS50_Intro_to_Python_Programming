from validator_collection import email, is_email

email_id = input("What's your email address? ")
# if email(email_id):
#     print("Valid")
# else:
#     print("Invalid")


if is_email(email_id):
    print("Valid")
else:
    print("Invalid")
