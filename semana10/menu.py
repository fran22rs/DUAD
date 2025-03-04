def show_menu():
    print("Menu:")
    print("1- Enter student information")
    print("2- View all students")
    print("3- View the top 3 students")
    print("4- View the average grade of all students")
    print("5- Export data to a CSV ")
    print("6- Import data from a CSV ")
    print("7- Exit")

def get_menu_option():
    while True:
        try:
            option = int(input("Select an option: "))
            if option < 1 or option > 7:
                print("Invalid option, enter a number between 1 and 7, no letters")
            else:
                return option
        except ValueError:
            print("enter a valid option")
