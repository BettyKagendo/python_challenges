#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''

#employee_registration
def employee_registration (file_name):
    with open ('user.txt', 'a') as file:
        while True:
            username = input ('Enter a username: ')
            password = input ('Enter a password: ' )
            confirm_password = input ('Confirm your password: ')

            if password != confirm_password:
                print ('Passwords do not match. Please try again')
            else:
                file.write (f"{username}, {password}\n")
                print ("Registration successful!")
                break
# login section
def user_login ():
    users = {}  #empty dictionary to store the username and passwords
    with open ('user.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(', ') # strip is for removing any whitespace characters
                users [username] = password 

    while True:
            username = input ("Enter your username: ")
            password = input ("Enter your password: ")

            if username in users and users [username] == password:
                print ("Login successful!")
                return username
            else:
                print ("Invalid username or password. Please try again!")

#function to add a new task
def add_task(tasks_file, logged_in_user):
    with open(tasks_file, 'a') as file:
        assigned_user = input("Enter the username of the person assigned to the task: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter the due date for the task (YYYY-MM-DD): ")
        assigned_date = datetime.date.today().strftime("%Y-%m-%d")
        task_completed = "No"

        task_details = f"{assigned_user}, {task_title}, {task_description}, {assigned_date}, {due_date}, {task_completed}\n"
        file.write(task_details)
        print("Task added successfully!")






                                 





while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        pass
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''

    elif menu == 'a':
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")