"""
banner id = B01888722
program name = Task 4
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

"""Function for displaying username and IP address"""
def display_uaip(varriable_dictionary):
    print(f"\nThis is the username: {varriable_dictionary["user_name"]}")
    print(f"This is the ip address: {varriable_dictionary["ip_address"]}\n")
    return

"""function for displaying the key and values of the dictionary"""
def display_dictionary(varriable_dictionary):
    for key, value in varriable_dictionary.items():
        print(f"{key}: {value}")
    return

"""function for adding something into the dictionary"""
def add_dictionary(varriable_dictionary):
    print(f"\nThis is the current dictionary: \n") #printing the current dictionary
    display_dictionary(varriable_dictionary) #displaying the current dictionary
    usin_key = input("Please input the key you would like to add into the dictionary: ") #asking the user for the key they want to delete
    while usin_key.strip() == "": #checking if the user input is empty
        print(f"\nThis is the current dictionary: \n") #printing the current dictionary
        display_dictionary(varriable_dictionary) #displaying the current dictionary
        usin_key = input("Invalid key, please try again: ") #asking the user to re-enter their key since it was invalid
    while usin_key in varriable_dictionary: #checking if the key is in the dictionary
        print(f"\nThis is in the current dictionary: \n") #printing the current dictionary
        display_dictionary(varriable_dictionary) #displaying the current dictionary
        usin_key = input("Please enter a different key: ") #asking the user to re-enter their key since it was invalid
        while usin_key.strip() == "": #checking if the user input is empty
            print(f"\nThis is the current dictionary: \n") #printing the current dictionary
            display_dictionary(varriable_dictionary) #displaying the current dictionary
            usin_key = input("Invalid key, please try again: ") #asking the user to re-enter their key since it was invalid
    usin_value = input(f"Please input the value for {usin_key}: ") #asking the user for the value of the key they want to add
    while usin_value.strip() == "": #checking if the user input is empty
        print(f"\nThis is the current dictionary: \n") #printing the current dictionary
        display_dictionary(varriable_dictionary) #displaying the current dictionary
        usin_value = input(f"Invalid value, please try again for {usin_key}: ") #asking the user to re-enter their value since it was invalid
    varriable_dictionary[usin_key] = usin_value #adding the new key-value pair to the dictionary
    return varriable_dictionary

"""Function for changing a value in the dictionary"""
def change_dictionary(varriable_dictionary):
    print(f"\nThis is the current dictionary: \n") #printing the current dictionary
    display_dictionary(varriable_dictionary) #displaying the current dictionary
    usin_change = input("Please input the key you would like to change from the dictionary: ") #asking the user for the key they want to delete
    while usin_change not in varriable_dictionary: #checking if the key is in the dictionary
        print(f"\nThis is the current dictionary: \n") #printing the current dictionary
        display_dictionary(varriable_dictionary) #displaying the current dictionary
        usin_change = input("Invalid key, please try again: ") #asking the user to re-enter their key since it was invalid
    usin_value = input(f"Please input the value for {usin_change}: ") #asking the user for the value of the key they want to add
    while usin_value.strip() == "": #checking if the user input is empty
        print(f"\nThis is the current dictionary: \n") #printing the current dictionary
        display_dictionary(varriable_dictionary) #displaying the current dictionary
        usin_value = input(f"Invalid value, please try again for {usin_change}: ") #asking the user to re-enter their value since it was invalid
    varriable_dictionary[usin_change] = usin_value #adding the new key-value pair to the dictionary
    return varriable_dictionary

"""Deleting an item from dictionary"""
def del_dictionary(varriable_dictionary):
    print(f"\nThis is the current dictionary: \n") #printing the current dictionary
    display_dictionary(varriable_dictionary) #displaying the current dictionary    usin = input("Please input the key you would like to delete from the dictionary: ") #asking the user for the key they want to delete
    usin_del = input("Please input the key you would like to delete from the dictionary: ") #asking the user for the key they want to delete
    while usin_del not in varriable_dictionary: #checking if the key is in the dictionary
        print(f"\nThis is the current dictionary: \n") #printing the current dictionary
        display_dictionary(varriable_dictionary) #displaying the current dictionary
        usin_del = input("Invalid key, please try again: ") #asking the user to re-enter their key since it was invalid
    del varriable_dictionary[usin_del] #deleting the key and value from the dictionary
    return varriable_dictionary


"""function for counting number of key value pairs in the dictionary"""
def count_dictionary(Varriable_dictionary):
    count = len(Varriable_dictionary)
    print(f"\nThere are {count} key value pairs in the dictionary")
    return

"""Main section of code"""
def main():

    varriable_dictionary = {
        "user_name":"Admin",
        "ip_address":"192.168.0.1",
        "event_type":"login",
        "risk_level":"low"
    }
    display_uaip(varriable_dictionary)
    print("\n")
    varriable_dictionary = add_dictionary(varriable_dictionary)
    print("\n")
    varriable_dictionary = change_dictionary(varriable_dictionary)
    print("\n")
    varriable_dictionary = del_dictionary(varriable_dictionary)
    print("\n")
    display_dictionary(varriable_dictionary)
    print("\n")
    count_dictionary(varriable_dictionary)

    
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