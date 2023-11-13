# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Saima Ahmed,11/10/2023,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str:str] = []  # dictionary of student data
students: list[dict[str:str]] = []  # a table of student data
file= None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

import json

# When the program starts, read the file data into a list of dictionary (table)

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print("File doesnt exist. Creating it...")
    print("----Technical Information----")
    print(e,e.__doc__,type(e),sep='\n')
finally:
    if not file.closed == True:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    # Input menu choice
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1": # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError ('First name should be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError ('Last name should be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data: dict[str:str] = {"First_name": student_first_name,\
                                           "Last_name": student_last_name,
                                           "Course": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name}\
 for {course_name}.")
            continue
        except ValueError as e:
            print(e)
            print("----Technical Information----")
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f"{student["First_name"]} {student["Last_name"]} is enrolled in {student["Course"]}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except Exception as e:
            print("----Technical Information----")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed == True:
                file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f"{student["First_name"]} {student["Last_name"]} is enrolled in {student["Course"]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
