"""
name = Task 02
banner id = B01888722
date start = 10/11/2026
date finish = 10/11/2026
"""
import random as r
from datetime import datetime
import socket as soc
from getpass import getpass

"""start of code"""

"""making a class for colors to make text look better"""
class color:
    bold: str = "\033[1m" #for making text bold
    red: str = "\033[91m" #for making text red
    yellow: str = "\033[93m" #for making text yellow
    end: str = "\033[0m" #for setting text back to normal

"""getting the users username and password"""
def getin():
    username = input("Please input your username: ") #getting username
    inpassword = getpass("Please input your password: ") #getting password and hiding what the user can see to be more secure

    return username, inpassword #returning username and password

"""checking if the user successfully logged in or not"""
def logineven(user, inpassword, password, username):
    if user == username and inpassword == password: #checking if both username and password match with thei hard coded counterparts
        return "Successful login"
    else:
        return "Failed login"

"""function for getting random security event id"""
def getid():
    eventid = r.randint(1000,9999) #assagining a random number for the event id
    return eventid #returning the event id

"""function for getting time"""
def gettime():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #getting the date and time and storing it as a varriable we can read
    return timestamp #returning the time stamp

"""function for getting users ip address"""
def getip():
    s = soc.socket(soc.AF_INET, soc.SOCK_DGRAM) #opening the socket, and telling it to use ipv4 and UDP
    s.connect(("8.8.8.8", 80)) #telling the port to use
    ip_address = s.getsockname()[0] #setting the pc's ip address and storing it in a varriable
    s.close() #closing the socket
    return ip_address

"""function for displaying"""
def display(user, loginevent, timestamp, ip_address, eventid):

    print(f"{color.bold}{color.yellow}\nSECURITY EVENT LOG{color.end}")
    print("==================")
    print(f"Event ID: {eventid}")
    print(f"Username: {user}")
    print(f"IP Address: {ip_address}")
    print(f"Event: {loginevent}")
    print(f"Timestamp: {timestamp}")

"""main section of the code"""
def main():
    while True:
        username = "admin" #setting a username the user has to input
        password = "Testing321!!" #setting a password the user has to input
        user, inpassword = getin() #calling function for getting input from user
    
        loginevent = logineven(user, inpassword, password, username) #calling function for getting the loginevent
        timestamp = gettime() #calling function for getting the time stamp
        ip_address = getip() #calling the function for getting the current computers ip address
        eventid = getid() #calling the function for getting the event id
        display(user, loginevent, timestamp, ip_address, eventid) #calling the function for printing

        if loginevent == "Successful login": #checking if the user input the right password, and if not to loop through again
            print("\nRight username and password was input, login successful")
            break #breaking the loop the code is in
        else:
            print("\nWrong username or password was input, failed login")

"""calling main function"""
if __name__ == "__main__":
    try:
        while True:
            print(f"{color.bold}---Welcome to the security event log program---{color.end}\n")
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