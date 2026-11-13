"""
name = Task 01
banner id = B01888722
date start = 10/11/2026
date finish = 10/11/2026
"""

"""start of code"""
"""function for getting input"""

def getin(password, inter):
    usin = input("Welcome\nPlease input your password: ") #asking the user for their password
    while usin != password: #loop for checking if the users input matches the password
        usin = input("Invalid password, please try again: ") #asking the user for another attempt
        inter = inter + 1 #adding a number to show how many attempts the user has made
        if usin == password:
            break
        if inter == 3: #checking if the user has made the maximum number of attempts
            print("You have reached the maximum number of attempts, please try again later.") #printing a message to the user
            exit() #exiting the program

"""function for choosing security event"""
def chooseevent():
    print("Please choose a security event from the list below:") #asking the user to choose a security event
    print("1. Security Event Counter") 
    print("2. Brute-Force Simulation") 
    print("3. Login Authentication") 
    print("4. Exit") 
    event = input("Please input your choice: ") #asking the user for their choice
    while event not in ["1", "2", "3", "4"]: #loop for checking if the users input is valid
        event = input("Invalid choice, please try again: ") #asking the user to reinput their choice
    return event
"""function for security event 1"""
def event1():
    print("Welcome to security event counter") #printing a message to the user
    Password = "blickingbots123" #setting password for the security event
    failed = 0 #setting the number of failed attempts to 0
    correct = 0 #setting the number of correct attempts to 0
    for i in range(1, 11): #loop for counting the number of attempts
        print(f"Attempt {i}") #printing the number of attempts
        usin = input("Please input the password: ") #asking the user for the password
        if usin != Password:
            failed += 1
        elif usin == Password:
            correct += 1
    precentage = (failed / 10) * 100 #calculating the percentage of correct attempts
    print("You have reached the maximum number of attempts, please try again later.") #printing a message to the user
    print(f"You have inputed the correct password {correct} times, and the wrong password {failed} times.") #printing a message to the user
    print(f"You have inputed the incorrect password {precentage}% of the time.") #printing a message to the user
    if failed > 5: #checking if the user has inputed the wrong password 6 or more times
        print("Alert!!! 6 or more attempt's have been the wrong password, account is close to being locked.") #printing a message to the user
"""function for security event 2"""
def event2(inter, password2):
    usin = input("Welcome to security brute force simulation\nPlease input the password: ") #asking the user for the password
    if usin == password2: #checking if the user has inputed the correct password
        print("Access granted.") #printing a success message    
    while usin != password2: #loop for checking if the users input matches the password
        usin = input("Invalid password, please try again: ") #asking the user for another attempt
        inter = inter + 1 #adding a number to show how many attempts the user has made
        if usin == password2: #checking if the user has inputed the correct password
            print("Access granted.") #printing a success message
            break #breaking the loop if the user has inputed the correct password
        elif inter == 10: #checking if the user has made the maximum number of attempts
            print("You have reached the maximum number of attempts, please try again later.") #printing a message to the user
            break #exiting the program
    
            
"""function for security event 3"""
def event3(inter, password2, username):
    print("Welcome to security login authentication") #printing a message to the user
    while True: #loop for the login authentication
        uname = input("Please input your username: ") #asking the user for the username
        password = input("Please input your password: ") #asking the user for the password
        if uname == username and password == password2:
            print("Access granted.") #printing a success message
            break #breaking the loop if the user has inputed the correct username and password
        elif uname != username and password != password2:
            print("Invalid username and password, please try again.") #printing a message to the user
        inter += 1 #setting the number of attempts to 1
        if inter == 4: #checking if the user has made the maximum number of attempts
            print("You have reached the maximum number of attempts, please try again later.") #printing a message to the user
            break #breaking the loop if the user has made the maximum number of attempts

"""main function"""
def main():
    password = "password123!" #setting the password
    password2 = "blickingbots123" #setting the password for the security events
    username = "admin" #setting the username for the security events
    inter = 1 #setting the number of attempts to 1
    getin(password, inter) #calling the function to get the users input
    print("Access granted.") #printing a success message
    while True: #loop for the security events
        event = chooseevent() #calling the function to choose a security event
        if event == "1": #checking if the user chose the first option
            event1() #calling the function for the first option
        elif event == "2": #checking if the user chose the second option
            event2(inter, password2) #calling the function for the second option
        elif event == "3": #checking if the user chose the third option
            event3(inter, password2, username) #calling the function for the third option
        elif event == "4": #checking if the user chose the fourth option
            print("Exiting program, thank you for using our security tool.") #printing a message to the user
            exit() #exiting the program

"""calling main function"""
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        exit()