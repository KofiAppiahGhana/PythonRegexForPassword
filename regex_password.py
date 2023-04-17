import re

print("""
    Enter any password to check if it is valid.
    The password must have the following:
        At least one uppercase character(A-Z)
        At least one lowercase character(a-z)
        Digits(0-9)
        special symbols
        Must be at least 6 characters long
""")


def password():
    user_password = input("Enter your password: ")
    if re.search(r"[A-Z]+", user_password) and re.search(r"[a-z]+", user_password) and\
            re.search(r"\d+", user_password) and re.search(r"[@#^&*%$!]", user_password) and len(user_password) >= 6:
        print("Password Accepted!")
    else:
        print("Password NOT accepted! Refer to the criteria!!")


password()
