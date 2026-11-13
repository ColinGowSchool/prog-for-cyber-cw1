# prog-for-cyber-cw1

# Name - Colin M Gow
# Student banner id - B01888722
# Campus - NCL Motherwell

# [main](https://github.com/ColinGowSchool/prog-for-cyber-cw1/blob/cyber-security-utilities/main.py)
## Main program instructions

Program will prompt the user to enter a password, if the password does not meet the specific specs, then it will tell the user what requirement it didn't meet

Then the program will prompt the user to enter an ip address, if the ip address is not valid, then it will display that it is invalid

If either ip address, or password is failed the it will run through the code again, and display a suggested password for the user that meets requirements

Once both requirements are met, the user will be prompted to go through the code again or to end the program

# [security_tools](https://github.com/ColinGowSchool/prog-for-cyber-cw1/blob/cyber-security-utilities/security_tools.py)

## where all the logic happens [not instructions just descriptions]

the first 2 functions are for the password checker, the bring in the password passed through then check the length, if theirs a number, if there's a special character, and if theirs any spaces, the first function checks and returns an integer which the second function checks against and returns either a false, or true with a message saying whether it passed or failed with what failed

the third and fourth functions are for checking the ip address, the third function checks the octets to make sure all 4 are between 0 and 255, if not it returns false (there's also a try in case of any unexpected errors that can occur which will return a false)

the fourth function will call the third function and check if any dots are detected, if not store a false, if there is store a true, then it checks how many dots there are, if there are 3 then store a true, otherwise store a false, then it calls the function to check the octets, if all validation checkers return true values it returns true, if it doesn’t then it will return a false

the fifth function will make up a strong password that is between 10-16 characters long, choose between symbols, have at least one capital letter, and one lowercase letter


# [Testing table with screenshots](https://github.com/ColinGowSchool/prog-for-cyber-cw1/blob/cyber-security-utilities/Testing%20table%20for%20task%205.docx)
This file has test tables with what steps I done in each part, and if the test failed, or passed
