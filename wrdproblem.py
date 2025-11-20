def funct(doEmail):
    if doEmail == True:
        emailvar = input("Please enter your email. >>>")
        emailvar.strip(" ")
        if emailvar.isdigit() is True:
            print("Your email is not valid! Email must be a string.")
            emailvar = None
            return "invalid"
        elif emailvar.find("@") == -1:
            print("Your email is not valid!  Must contain an @ symbol.")
            emailvar = None
            return "invalid"
        print(f"Email validated: {emailvar}")
        return emailvar
    
    else:
        print("doEmail was not True, doing password process")   
        upperCheck = False
        numCheck = False
        letterCount = 0
        print("Please enter a password. The password MUST contain atleast 8 characters, 1 digit, and 1 uppercase letter.")
        passwordvar = input(">>>")
        for i in passwordvar:
            if i.isupper() == True:
                print("Uppercase check OKAY")
                upperCheck = True
            if i.isdigit() == True:
                print("Num check OKAY")
                numCheck = True
            letterCount += 1
        if letterCount <= 8:
            print("Your password is not valid! Must be atleast 8 characters in length.")
            passwordvar = None
            return "invalid"
        else:
            print("Letter check OKAY")
        if upperCheck == False:
            print("Your password is not valid! upperCheck was False.")
            passwordvar = None
            return "invalid"
        elif numCheck == False:
            print("Your password is not valid! letterCheck was False.")
            passwordvar = None
            return "invalid"
        print(f"Password validated: {passwordvar}")
        return passwordvar

password = None    
email = None

checkFin = False
while checkFin == False:
    if email == None:
        email = funct(True)
        if email == "invalid":
            email == None
            continue
    if password == None:
        password = funct(False)
        if password == "invalid":
            password = None
            continue
    else:
        checkFin = True
        print("email & password has been validated")
        print(password)
        print(email)

    
