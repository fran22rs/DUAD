def validate_grade(subject_name):
    while True:
        try:
            grade = float(input(f"enter the grade for {subject_name} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: grade must be between 0 and 100! Try again")
        except ValueError:
            print("Error: enter a valid number! Try again")

def add_student():
    print("Enter the details for the student:")

    full_name = input("Full name: ")
    section = input("Section (for example, 7A or 10C): ")

    print("Enter the grades (must be between 0 and 100):")
    spanish_grade = validate_grade("Spanish")
    english_grade = validate_grade("English")
    social_studies_grade = validate_grade("Social Studies")
    science_grade = validate_grade("Science")

    student_data = {
        "Full Name": full_name,
        "Section": section,
        "Spanish Grade": spanish_grade,
        "English Grade": english_grade,
        "Social Studies Grade": social_studies_grade,
        "Science Grade": science_grade
    }

    print(f"Student data entered: {student_data}")  
    return student_data

def display_student_data(students_list):
    if not students_list:
        print("No students found.")
        return

    print("Entered student data:")
    for student in students_list:
        print("Student:")
        for key, value in student.items():
            print(f"{key}: {value}")
        print("-" * 40)  

def calculate_average(student):
    return (student["Spanish Grade"] + student["English Grade"] + student["Social Studies Grade"] + student["Science Grade"]) / 4

def top_3_students(students_list):
    sorted_students = sorted(students_list, key=lambda student: calculate_average(student), reverse=True)
    print("Top 3 students with the highest average:")
    for i in range(min(3, len(sorted_students))):
        student = sorted_students[i]
        average = calculate_average(student)
        print(f"{i+1}-{student['Full Name']} - Average: {average}")

def overall_average(students_list):
    total_average = 0
    for student in students_list:
        total_average += calculate_average(student)
    return total_average / len(students_list) if students_list else 0
