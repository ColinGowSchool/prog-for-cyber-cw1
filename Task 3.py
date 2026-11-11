"""
banner id = B01888722
program name = Task 03
date start = 10/11/2026
date finish = 10/11/2026
"""


"""Start of program"""

"""making a class for colors to make text look better"""
class color:
    bold: str = "\033[1m" #for making text bold
    red: str = "\033[91m" #for making text red
    yellow: str = "\033[93m" #for making text yellow
    end: str = "\033[0m" #for setting text back to normal

"""function for checking entered ip address octects"""
def check_number_amount_ipaddress(user_input):
    """
    This function is for making sure each octect is within 256
    And returns a true or false
    """
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

"""function for checking ip address entered is a valid ip address"""
def check_ip_address(user_input):

    """
    calling function to get user input for their ip address
    then stripping any spaces from it
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

"""function for add an ip address"""
def ipaddress_input(ip_list):
    """
    user enters an ip address
    a function to check weather the ip is validate is called to check user input
    loops until the ip entered is valid and returns the new list of ip addresses
    """
    while True:
        add_user_ipaddress = input("\nPlease input the if address you want to input: ")
        validation = check_ip_address(add_user_ipaddress)
        if validation == True:
            ip_list.append(add_user_ipaddress)
            return ip_list
        else:
            print("Invalid IP address, please try again.\n")
    
"""function for removing an ip address the user entered"""
def rem_ip_address(ip_list):
    """
    printing all current ip addresses in the list
    then asking the user for the ip address they want to delete
    then running through each entry in the list till it matches then returning the list
    """
    number = 0
    print("Current list of ip address:")
    for line in ip_list:
        print(line)
    usr_input = input("\nPlease enter the ip address you'd like removed: ")
    if usr_input not in ip_list:
        print("IP address not found inside of the current ip list\n")
        return ip_list
    for line in ip_list:
        if line == usr_input:
            del ip_list[number]
        else:
            number = number + 1
    if usr_input not in ip_list:
            print(f"{color.bold}{color.yellow}IP address removed from ip list\n{color.end}")
    return ip_list

"""function for look for a specific ip address in the list"""
def ip_address_find_entry(ip_list):
    """
    In this function the user enters an ip address they want to find
    if the ip address isn't found then it prints saying it was found
    else if it was found then it displays where it is inside the list
    """
    while True:
        find_ip_entry = input("\nWhat IP address would you like to look for?: ")
        valid = check_ip_address(find_ip_entry)
        if valid == True:
            if find_ip_entry in ip_list:
                print(f"{color.bold}IP is in list of IP addresses{color.end}")
                return ip_list
            else:
                print(f"{color.bold}Ip address is not within the ip addres{color.end}")
                return ip_list
        else:
            print("IP address was no valid, please try again")

"""Function for counting amount of ips in list"""
def ip_address_list_count(ip_list):
    """
    This function will loop through the list of ips and count how many are detected
    then it will display how many ips there are inside of the array
    """
    number = 1
    for line in ip_list:
        number = number + 1
    print(f"\nThere are currently [{number}] in the ip address list")
    return ip_list


"""main section of program"""
def main():
    """
    this is the main program, this is where we print everything out, and call all functions (besides main)    
    """
    print(f"\n{color.bold}=============================")
    print("Hello, and welcome to the suspicious IP program")
    print("In this program, we'll look at suspicious IP address detected")
    print("And let you add one in, remove one the user wants, and search for one the user wants")
    print(f"============================={color.end}\n")
    suspicious_ipaddress = [
        "192.168.4.25",
        "192.168.0.42",
        "192.168.52.46",
        "192.64.12.42"
    ]

    print("The first suspicious IP address is: ", suspicious_ipaddress[0])
    print("The last suspicious IP address is: ", suspicious_ipaddress[-1])
    suspicious_ipaddress = ipaddress_input(suspicious_ipaddress)
    suspicious_ipaddress = rem_ip_address(suspicious_ipaddress)
    suspicious_ipaddress = ip_address_find_entry(suspicious_ipaddress)
    suspicious_ipaddress = ip_address_list_count(suspicious_ipaddress)
    
        
"""calling main function"""
if __name__ == "__main__":
    try:
        while True:
            main()
            bolean = input("Would you like to go through the code again?(y/n): ") #asking the user wants to repeat the program
            while bolean.lower() not in ["y", "n"]: #validating their answer
                bolean = input("Invalid input, please try again(y/n): ") #asking them to re-enter their input since it was invalid

            if bolean.lower() == "y": #checking if the user input y to loop through again
                print("Going through the code again\n")
            elif bolean.lower() =="n": #checking if the user input n to stop the loop
                print(f"{color.bold}\nEnding code, thank you for using the security event program")
                print(f"---Goodbye!---{color.end}")
                exit() #exiting program

    except KeyboardInterrupt: #incase user inputs a interrupt command through their keyboard
        print(f"{color.bold}{color.red}\n\nUser has input an interrupt command, stoping")
        print(f"---Goodbye!---{color.end}")

    except Exception as e: #incase any error unknown comes up, will store it as e so it can be printed later
        print(f"{color.bold}{color.red}\n\nAN ERROR OCCURED")
        print(f"Error: {e}") #displaying the error that occured with the earlier varriable 
        print("ending program")
        print(f"---Goodbye!---{color.end}")
        exit() #exiting the code