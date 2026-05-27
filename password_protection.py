#password_protection.py
#The purpose of this program is to help users avoid common weak passwords

#Initialize
import pandas as pd
import time
data = pd.read_csv('Passwords.csv') #Accessing data from a spreadsheet called passwords

id = data['id'].tolist() #Assigns a number for the password among the list of 500 in an array
rank = data['rank'].tolist() #The ranking of the passwords popularity in an array
password = data['password'].tolist() #A list of the various passwords stored in an array
category = data['category'].tolist() #Describes the theme that the password falls under in an array
value = data['value'].tolist() #The unit value for the time unit measurement in an array
time_unit = data['time_unit'].tolist() #A unit of time used to measure how long it would take to crack the password in an array
strength = data['strength'].tolist() #A score ranking given to a certain password in an array

filter = [] #The empty array used to filter data

#Functions
def common_pass(number):   #This command allows users to input a password and if it is in the top 500 most common passwords the program prints what its ranking.
    for i in range(len(id)):
        if rank[i] == number:
            filter.append(password[i])
    if filter == []:
        print("Your number is not is not between 1-500, please try again")
    else:
        print(f"{filter} is the {number} most common password")
        filter.clear()

def protection(eval):     #This command allows users to input a password to see its strength and how long it would take to crack that password.
    for i in range(len(id)):
        if eval == password[i]:
            filter.append(strength[i])
            filter.append(value[i])
            filter.append(time_unit[i])
    if filter == []:
        print(f"{eval} is not in our database for the top 500 most common passwords, maybe try another one")
    else:
        print(f'The password, "{eval}" has a strength of {filter[0]}; It would take {filter[1]} {filter[2]} to crack')
    filter.clear()

def top_10():            #This command allows users to see the top 10 most commonly used passwords.
    for i in range (10):
        print(f"{rank[i]}: {password[i]}")

def strong(word):
    for i in range(len(password)):
        if word == password[i]:
            filter.append(password[i])
            filter.append(strength[i])
    if filter == []:
        print(f"{word} is not in our database for the top 500 most common passwords, maybe try another one")
    else:
        if filter[1] >= 10:
            print(f"{filter[0]} is strong as it has a strength greater than 10")
        elif filter[1] < 10:
            print(f"{filter[0]} is weak as it has a strength less than 10")
        filter.clear()
def menu(): #Creating the main menu for users to interact with in order to execute different commands
    while True:
        main = input("""Welcome to our list of the top 500 most common passwords. What do you want to inquire about? Pick a number to access a command.
    1) Get the top 10 most common passwords
    2) See which place a password will fall in the rankings
    3) Determine how long would it take to crack a password
    4) Figure out if a password is strong
    5) Exit
What number are you thinking:
    """)

        if main == "1" or main == "1)": #Executes top_10 command
            time.sleep(2)
            print("Here are the top 10 passwords! ")
            top_10()
        elif main == "2" or main == "2)": #Executes common_pass command
            number = input("Input an integer number between 1-500 to see its ranking: ")
            if number.isdigit() == True:
                common_pass(int(number))
            else:
                print("Not an integer between 1-500")
        elif main == "3" or main == "3)": #Executes protection command
            eval = input("Tell us a password: ")
            protection(eval)
        elif main == "4" or main == "4)": #Executes strong command
            word = input("Type a password and we will tell you if it is strong: ")
            strong(word)
        elif main == "5" or main == "5)": #If the user wishes to exit the code, they can type 5
            print("exitttingggg...")
            break
        else:                    #If the user inputs something not between 1-5 the program will respond with stating that whatever was typed, was not an option
            print(f"'{main}' isn't an option, try again")
            time.sleep(2)
#Main

menu()

#Sources of Information

#Data about password strength
#Website Name: Github.com & Code.org
#URL: https://github.com/rfordatascience/tidytuesday/blob/main/data/2020/2020-01-14/passwords.csv
#Author Name: jthomasmock
#Article Name: passwords.csv
#Date written: 2025-01-14
