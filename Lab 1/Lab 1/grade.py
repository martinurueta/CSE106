import json

def create_student_grade(student_dict, name, grade):
    student_dict[name] = grade
    return student_dict

def get_student_grade(student_dict, name):
    return student_dict.get(name)

def edit_student_grade(student_dict, name, new_grade):
    student_dict[name] = new_grade
    return student_dict

def delete_student_grade(student_dict, name):
    student_dict.pop(name, None)
    return student_dict

def save_to_file(student_dict):
    with open("grades.txt", "w") as f:
        json.dump(student_dict, f)

def load_from_file():
    try:
        with open("grades.txt", "r") as f:
            student_dict = json.load(f)
            return student_dict
    except:
        return {}



        

student_dict = load_from_file()
while True:
    print("1. Create Student and Grade")
    print("2. Get Student Grade")
    print("3. Edit Student Grade")
    print("4. Delete Student Grade")
    print("5. Save and Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_dict = create_student_grade(student_dict, name, grade)
    elif choice == 2:
        name = input("Enter student name: ")
        grade = get_student_grade(student_dict, name)
        if grade:
            print(f"{name}'s grade is {grade}")
        else:
            print("Student not found")
    elif choice == 3:
        name = input("Enter student name: ")
        grade = get_student_grade(student_dict, name)
        if grade:
            new_grade = input("Enter new grade: ")
            student_dict = edit_student_grade(student_dict, name, new_grade)
            print(f"{name}'s grade is updated to {new_grade}")
        else:
            print("Student not found")
    elif choice == 4:
        name = input("Enter student name: ")
        grade = get_student_grade(student_dict, name)
        if grade:
            student_dict = delete_student_grade(student_dict, name)
            print(f"{name} and their grade are deleted")
        else:
            print("Student not found")
    elif choice == 5:
        save_to_file(student_dict)
        print("Grades saved and program exited")
        break
    else:
        print("Invalid choice. Try again")
