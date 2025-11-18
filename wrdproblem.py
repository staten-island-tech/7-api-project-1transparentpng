password = None
email = input("Please enter your email. >>>")

def validateEmail(input):
    input.strip(" ")
    if input.find("@") == -1:
        print("Your email is not valid!  Must contain an @ symbol.")
        return "invalid"
    else:
        print(f"Email validated: {input}")
        return "valid"

if validateEmail(email) == "invalid":
    exec(email)