# Global dictionary to store student marks
students_marks = {}

# Function to get student data
def get_student_data():
    name = input("Enter the student's name: ")
    marks = int(input(f"Enter marks for {name}: "))
    return name, marks

# Function to collect multiple student data
def collect_students_data():
    global students_marks  # Use the global students_marks variable
    num_students = int(input("How many students' data would you like to enter? "))
    
    for _ in range(num_students):
        name, marks = get_student_data()  # Get individual student's data
        students_marks[name] = marks      # Store in the dictionary

    print("Records have been created.")

# Function to update student data
def update():
    name = input("Enter the student's name to update: ")
    if name in students_marks:
        new_marks = int(input(f"Enter new marks for {name}: "))
        students_marks[name] = new_marks
        print("Record updated.")
    else:
        print("Student not found.")

# Function to delete student data
def delete():
    name = input("Enter the student's name to delete: ")
    if name in students_marks:
        del students_marks[name]
        print(f"Record for {name} deleted.")
    else:
        print("Student not found.")

# Function to search for student data
def search():
    name = input("Enter the student's name to search: ")
    if name in students_marks:
        print(f"Student: {name}, Marks: {students_marks[name]}")
    else:
        print("Student not found.")

# Function to view all student data
def view_data():
    if students_marks:
        print("Student Marks Dictionary:")
        for name, marks in students_marks.items():
            print(f"{name}: {marks}")
    else:
        print("No data available.")

# Function to exit the application
def exit_app():
    print("Thank you, execution ended.")
    exit()

# Function to get menu options
def get_menu():
    menu = {
        1: collect_students_data,  # Create (collect data)
        2: delete,                  # Delete record
        3: update,                  # Update record
        4: search,                  # Search record
        5: view_data,               # View all data
        6: exit_app                 # Exit
    }
    return menu

# Function to start the app and display menu
def start_app():
    while True:
        print("\n1-create, 2-delete, 3-update, 4-search, 5-view data, 6-exit")
        choice = input('Enter your choice: ')
        
        # Check if the input choice is valid
        if choice.isdigit() and int(choice) in get_menu():
            menu = get_menu()
            # Call the function corresponding to the choice
            menu[int(choice)]()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        # Ask if the user wants to continue or exit
        continue_choice = input('Enter 1 to continue and any other number to exit: ')
        if continue_choice != '1':
            print("Thank you, execution ended.")
            break

# Start the application
start_app()
