import csv

def import_from_csv():
    filename = input("Enter the filename to import data:")
    
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            existing_students = [student for student in reader]
            print(f"Data imported successfully from {filename}.")
            return existing_students
    except FileNotFoundError:
        print(f"{filename} was not found, make sure you have exported data before.")
        return [] 
    except Exception as ex:
        print(f"Error importing data: {ex}")
        return []

def export_to_csv(new_students):
    filename = input("To save data, enter the file name: ")
    
    try:
        existing_students = import_from_csv()
        all_students = existing_students + new_students
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Full Name", "Section", "Spanish Grade", "English Grade", "Social Studies Grade", "Science Grade"])
            writer.writeheader()
            for student in all_students:
                writer.writerow(student)
        print(f"Data successfully exported to {filename}.")
    except Exception as ex:
        print(f"Error exporting data: {ex}")
