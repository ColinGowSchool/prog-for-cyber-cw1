"""
banner id = B01888722
program name = security_tools
date start = 10/11/2026
date finish = 10/11/2026
"""
#start of program

"""making a class for colors to make text look better"""
import random
import string

class color:
    bold: str = "\033[1m" #for making text bold
    red: str = "\033[91m" #for making text red
    yellow: str = "\033[93m" #for making text yellow
    end: str = "\033[0m" #for setting text back to normal

"""function for checking entered password"""
def passcheck(password):
    checklen = len(password) #checking the length of the password

    checkcap = len([c for c in password if c.isupper()]) #checking how many characters are uppercase

    checklow = len([c for c in password if c.islower()]) #checking how many lower characters there are

    checknum = len([c for c in password if c.isdigit()]) #checking how many digits there are

    checkspec = len([c for c in password if c in "!@#$%"]) #checking to see if any of these predefined special characters are there

    checkspace = len([c for c in password if c.isspace()]) #checking to see if theres any spaces

    return checklen, checkcap, checklow, checknum, checkspec, checkspace # returning all varaiables

"""function for validating the password"""
def validate_checker(password):
    checklen, checkcap, checklow, checknum, checkspec, checkspace = passcheck(password) #calling the function that analyses the password

    if checklen < 10: #checking if the length is met
        return False, f"{color.red}Password must be at least 10 characters long.\n{color.end}" #returning a message, and a bolean

    if checkcap < 1: #checking if captial letter requirement is met
        return False, f"{color.red}Password must contain at least 1 uppercase letter.\n{color.end}" #returning a message, and a bolean

    if checklow < 1: #checking if lower letter requirement is met
        return False, f"{color.red}Password must contain at least 1 lowercase letter.\n{color.end}" #returning a message, and a bolean

    if checknum < 1: #checking if the number requirement is met
        return False, f"{color.red}Password must contain at least 2 digits.\n{color.end}" #returning a message, and a bolean

    if checkspec < 1: #checking if the special predefined characters requirement is met
        return False, f"{color.red}Password must contain at least 1 special character from !@#$%.\n{color.end}" #returning a message, and a bolean

    if checkspace > 0: #checking if the space requirement is met
        return False, f"{color.red}Password must not contain any spaces.\n{color.end}" #returning a message, and a bolean

    return True, f"{color.bold}{color.yellow}\nPassword is valid.{color.end}" #returning a message, and a bolean

"""function for checking ip address's octects"""
def check_number_amount_ipaddress(user_input):
    octects = user_input.split(".")
    octect_counter = 0
    try:
        if int(octects[0]) < 256 and int(octects[0]) >= 0:
            octect_counter = octect_counter + 1
        else:
            return False
    
        if int(octects[1]) < 256 and int(octects[1]) >= 0:
            octect_counter = octect_counter + 1
        else:
            return False
    
        if int(octects[2]) < 256 and int(octects[2]) >= 0:
            octect_counter = octect_counter + 1
        else:
            return False
    
        if int(octects[3]) < 256 and int(octects[3]) >= 0:
            octect_counter = octect_counter + 1
        else:
            return False
        if octect_counter == 4:
            return True

    except Exception as e:
        return False
    
"""function for calling relevant functions and checking the ip address"""
def check_ip_address(user_input):

    """
    stripping any spaces from ip address
    then calling function to check the octects of the ip address
    then checking if theres any dots, and how many dots there are
    """


    user_input = user_input.strip()



    check_how_many_dot = len([c for c in user_input if c in "."])
    if check_how_many_dot > 0:
        dot_validation = True
    elif check_how_many_dot < 1:
        dot_validation = False

    
    if check_how_many_dot == 3:
        dot_count = True
    else:
        dot_count = False
    check_number_in_ip = len([c for c in user_input if c.isdigit()])
    if check_number_in_ip > 3:
        number_validation = True
    else:
        number_validation = False

    octect_validation = check_number_amount_ipaddress(user_input)
    

    if dot_validation == True and dot_count == True and number_validation == True and octect_validation == True:
        return True
    else:
        return False


def generate_strong_password():

    length = random.randint(10, 16)
    symbols = "!@#$%"
    pw = [random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits),
    random.choice(symbols)]
    pool = string.ascii_letters + string.digits + symbols
    pw += [random.choice(pool) for _ in range(length - 4)]
    random.shuffle(pw)
    return "".join(pw)