# #=====importing libraries===========
# '''This is the section where you will import libraries'''
import datetime

# #====Login Section====
# '''Here you will write code that will allow a user to login.
#     - Your code must read usernames and password from the user.txt file
#     - You can use a list or dictionary to store a list of usernames and passwords from the file
#     - Use a while loop to validate your user name and password
# '''

# #  admin credentials
admin_username = 'admin'
admin_password = 'adm1n'

# #function to check whether user is admin
def is_admin (username, passsword):
     return username == admin_username and passsword == admin_password:
        


# #employee_registration
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
#         assigned_date = datetime.date.today().strftime("%Y-%m-%d")
#         task_completed = "No"

#         task_details = f"{assigned_user}, {task_title}, {task_description}, {assigned_date}, {due_date}, {task_completed}\n"
#         file.write(task_details)
#         print("Task added successfully!")


# # view all tasks function
# def view_all_tasks(tasks_file):
#     with open(tasks_file, 'r') as file:
#         tasks = file.readlines()
#         if not tasks:
#             print("No tasks found.")
#         else:
#             print("All Tasks:")
#             for task in tasks:
#                 task_details = task.strip().split(', ') #splits task into a list of values separated by a comma
#                 assigned_user = task_details[0] #The subsequent lines assign each component of task_details
#                 task_title = task_details[1]  #to separate variables e.g assigned_user using indexing
#                 task_description = task_details[2]
#                 assigned_date = task_details[3]
#                 due_date = task_details[4]
#                 task_completed = task_details[5]
#                 print(f"Assigned User: {assigned_user}, Task Title: {task_title}, Task Description: {task_description}, Assigned Date: {assigned_date}, Due Date: {due_date}, Completed: {task_completed}")
#                 print("-" * 20)  # to visually separate the details of each task


# #view my tasks

# def view_my_tasks(tasks_file, logged_in_user):
#     with open(tasks_file, 'r') as file:
#         tasks = file.readlines()

#     user_tasks = [task for task in tasks if task.strip().split(', ')[0] == logged_in_user]

#     if not user_tasks:
#         print("You have no tasks assigned.")
#     else:
#         print(f"Tasks assigned to {logged_in_user}:")
#         for task in user_tasks:
#             task_details = task.strip().split(', ')
#             print(f"Assigned User: {task_details[0]}")
#             print(f"Task Title: {task_details[1]}")
#             print(f"Task Description: {task_details[2]}")
#             print(f"Assigned Date: {task_details[3]}")
#             print(f"Due Date: {task_details[4]}")
#             print(f"Completed: {task_details[5]}")
#             print("-" * 20)



# while True:
#     # Present the menu to the user and 
#     # make sure that the user input is converted to lower case.
#     menu = input('''Select one of the following options:
# r - register a user
# a - add task
# va - view all tasks
# vm - view my tasks
# e - exit
# :''').lower()

#     if menu == 'r':
#         employee_registration('user.txt')
#         '''This code block will add a new user to the user.txt file
#         - You can use the following steps:
#             - Request input of a new username
#             - Request input of a new password
#             - Request input of password confirmation.
#             - Check if the new password and confirmed password are the same
#             - If they are the same, add them to the user.txt file,
#               otherwise present a relevant message'''

#     elif menu == 'a':
#         logged_in_user = user_login()
#         if logged_in_user:
#             add_task('tasks.txt', logged_in_user)
#         else:
#             print("Login failed. Cannot add a task.")

        
#         '''This code block will allow a user to add a new task to task.txt file
#         - You can use these steps:
#             - Prompt a user for the following: 
#                 - the username of the person whom the task is assigned to,
#                 - the title of the task,
#                 - the description of the task, and 
#                 - the due date of the task.
#             - Then, get the current date.
#             - Add the data to the file task.txt
#             - Remember to include 'No' to indicate that the task is not complete.'''

#     elif menu == 'va':
#          view_all_tasks('tasks.txt')
        
#          '''This code block will read the task from task.txt file and
#          print to the console in the format of Output 2 presented in the PDF
#          You can do it in this way:
#             - Read a line from the file.
#             - Split that line where there is comma and space.
#             - Then print the results in the format shown in the Output 2 in the PDF
#             - It is much easier to read a file using a for loop.'''

#     elif menu == 'vm':  
#         logged_in_user = user_login()
#         if logged_in_user:
#             view_my_tasks('tasks.txt', logged_in_user)
#         else:
#              print("Login failed. Cannot view your tasks.")
    
    
#         '''This code block will read the task from task.txt file and
#          print to the console in the format of Output 2 presented in the PDF
#          You can do it in this way:
#             - Read a line from the file
#             - Split the line where there is comma and space.
#             - Check if the username of the person logged in is the same as the 
#               username you have read from the file.
#             - If they are the same you print the task in the format of Output 2
#               shown in the PDF '''

#     elif menu == 'e':
#         print('Goodbye!!!')
#         exit()

#     else:
#         print("You have entered an invalid input. Please try again")