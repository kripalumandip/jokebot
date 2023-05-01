# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "admin.py" program of Project
# of CSI6208 in Semester 1, 2023.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json



# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSI6208 Requirement: Also enforce a minimum value of 1.  See assignment brief.
def inputInt(prompt):
    while True:
        user_input = input(prompt)
        if str(user_input).isdigit():
            if int(user_input) > 0:
                return user_input
            else:
                print("Please enter a minimum value of 1")
        else:
            print("Please enter a positive number.")
        



# This function repeatedly prompts for input until something (not whitespace) is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    while True:
        something = input(prompt)
        if something.strip():
            return something
        else:
            print("Please enter something")




# This function opens "data.txt" in write mode and writes dataList to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveChanges(dataList):
    with open('data.txt', 'w') as f:
        json.dump(dataList, f, indent=4)




# Here is where you attempt to open data.txt and read the data / create an empty list if the file does not exist.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

data = []

try:
    with open('data.txt', 'r') as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    pass


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Joke Bot Admin Program.')

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() # Prompt for input and convert it to lowercase.
        
    if choice == 'a':
        # Add a new joke.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        setup = inputSomething("Enter the setup: ")
        punchline = inputSomething("Enter the punchline: ")
        numOfRatings = 0
        sumOfRatings = 0
        data1 = {"setup": setup, "sumOfRatings": sumOfRatings, "punchline": punchline, "numOfRatings": numOfRatings}
        data.append(data1)
        print("Joke added successfully")
        saveChanges(data)


    
    elif choice == 'l':
        # List the current jokes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        i = 0
        if len(data) == 0:
            print("No jokes saved")
        else:
            print("List of Jokes.")
            for data1 in data:
                #print("Joke number:", i + 1)
                print(i+1,".",data1['setup'])
                #print("Sum of Ratings:",data1['sumOfRatings'])
                #print("Punchline:",data1['punchline'])
                #print("Num of Ratings:",data1['numOfRatings'])
                i += 1



    elif choice == 's':
        # Search the current jokes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        i = 0
        search_term = inputSomething("Enter the search term: ").lower()
        for data1 in data:
            if search_term in (data1['setup']).lower() or search_term in (data1['punchline']).lower():
                print(i + 1,'.',data1['setup'])
                # print('->',data1['punchline'])
            i += 1



    elif choice == 'v':
        # View a joke.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.

        index_number = inputInt("Enter Joke number: ")
        index_number = int(index_number)
        if index_number > len(data):
            print("Invalid Joke number")
        elif not data:
            print("No jokes saved")
        else:
            print(data[index_number-1]['setup'])
            print(data[index_number-1]['punchline'])
            if int(data[index_number-1]['numOfRatings']) == 0:
                print("Joke has not been rated yet")
            else:
                print("Joke is rated",data[index_number-1]['numOfRatings'],"time(s).")


    elif choice == 'd':
        # Delete a joke.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        index_number = inputInt("Enter Joke number to delete: ")
        index_number = int(index_number)
        if index_number > len(data):
            print("Invalid Joke number")
        elif not data:
            print("No jokes saved")
        else:
            del data[index_number - 1]
            print("Joke deleted successfully")
            saveChanges(data)

        

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Good Bye")
        break



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice.Please enter again.")
