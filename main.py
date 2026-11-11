"""
banner id = B01888722
program name = main
date start = 10/11/2026
date finish = 10/11/2026
"""

"""start of program"""
import security_tools as st
"""making a class for colors to make text look better"""

class color:
    bold: str = "\033[1m" #for making text bold
    red: str = "\033[91m" #for making text red
    yellow: str = "\033[93m" #for making text yellow
    end: str = "\033[0m" #for setting text back to normal


def main():
    #loop to validate password and ip address
    while True:
        password = input("Please enter a password: ") #asking the user to input a password
        valid, message = st.validate_checker(password) #calling the function that checks if the password is valid or not
        print(message) #printing the message that was returned from the function
        ip_address = input("Please enter an IP address: ") # geting the ip address from the user
        valid_ip = st.check_ip_address(ip_address) # caling function fot check the ip address
        if not valid_ip: #checking if the ip address is valid or not then displaying such
            print(f"{color.red}IP address is invalid{color.end}") #printing a message if the ip address is invalid
        else:
            print(f"{color.bold}{color.yellow}\nIP address is valid{color.end}") #printing a message if the ip address is valid
        strong_password = st.generate_strong_password() # calling function from st to generate a strong password that meets any requirements
        if valid and valid_ip: # checking if the ip address and password were valid 
            print(f"{color.bold}{color.yellow}\nPassword and IP address are valid, ending program{color.end}")
            break
        elif not valid: # checking if the password was invalid, and if so print a strong password that is recommended
            print(f"{color.red}Password is invalid{color.end}")
            print(f"here is a suggested password that meets the requirements: {strong_password}")

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