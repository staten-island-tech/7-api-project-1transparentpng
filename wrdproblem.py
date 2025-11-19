def funct():
    
    emailValidated = False
    email.strip(" ")
    if type is True:
        print("Your email is not valid! Email must be a string.")
        email = None
        return "invalid"
    elif email.find("@") == -1:
        print("Your email is not valid!  Must contain an @ symbol.")
        email = None
        return "invalid"
    else:
        print(f"Email validated: {email}")
        emailValidated = True    
    upperCheck = False
    numCheck = False
    letterCheck = 0
    password = input(">>>")
    for i in password:
        if i.isupper == True:
            print("Uppercase check OKAY")
            upperCheck = True
        if i.isdigit == True:
            print("Num check OKAY")
            numCheck = True
        letterCount += 1
    if letterCount <= 8:
        print("Your password is not valid! Must be atleast 8 characters in length.")
        return "invalid"


password = None    
email = None



    
