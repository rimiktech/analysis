#write a function "email_slicer" and find the user name and domain?#
def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} & domain is {domain}"
user_input = input("Enter Your Email: ")
print(email_slicer(user_input))