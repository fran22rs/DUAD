from menu import show_menu, get_menu_option
from students_data import (
    add_student, display_student_data, calculate_average, 
    top_3_students, overall_average
)
from exportimportdata import export_to_csv, import_from_csv


students_list = []

def main():
    global students_list 
    while True:
        show_menu()  
        option = get_menu_option()  

        if option == 1:  
            while True:
                try:
                    amount = int(input("How many students would you like to enter? "))
                    if amount < 1:
                        print("You need to enter at least one student")
                    else:
                        break  
                except ValueError:
                    print("Error: Please enter a valid number.")

            for i in range(amount): 
                student_data = add_student()  
                students_list.append(student_data)
            print(f"Student data entered successfully!")
            print(f"Current students list: {students_list}")  
            print(f"Total students: {len(students_list)}") 

        elif option == 2:  
            print(f"Displaying all students, Total students: {len(students_list)}") 
            if len(students_list) == 0:
                print("No students found")
            else:
                display_student_data(students_list)  
        elif option == 3: 
            top_3_students(students_list) 
        elif option == 4: 
            average = overall_average(students_list) 
            print(f"Overall average of all students: {average:.2f}")
        elif option == 5:  
            export_to_csv(students_list)
        elif option == 6: 
            students_list = import_from_csv() 
        elif option == 7: 
            print("Exit")
            break 
        
if __name__ == "__main__":
    main()