
# *************** Student Grade Management System *********


# features:-

# > Add students name and grades.
# > View all students and their grades.
# > Update a students
# > Delete a student 
# > Calculate marks(pass/fail)

student_grades = { }
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")

def view_all_students():
    if student_grades:
        for name , grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No Students found!")

def update_students(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

def delete_students(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

def calculated_marks(name,grade):
    if not student_grades:
        print("no student data avilable.")
    else:
        print("\nstudent grades: ")
        for name, grade in student_grades.items():
            status = "pass" if grade >=40 else "fail"
            print(f"{name} - grade: {grade},status: {status}")

def main():
    while True:
        print("\n STUDNET GRADES MANAGEMANT SYSTEM")
        print("1. Add student")
        print("2. View student")
        print("3. update student")
        print("4. delete student")
        print("5. calculated passing and fail student")
        print("6. exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name =")
            grade = int(input("Enter student " \
            "grade= ="))
            add_student(name,grade)

        elif choice == 2:
            view_all_students()

        elif choice == 3:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade ="))
            update_students(name,grade)

        elif choice == 4:
            name = input("Enter student name = ")
            delete_students(name)

        elif choice == 5:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade ="))
            calculated_marks(name,grade)

        elif choice == 6:
            print("closing the program")
            break
        else:
            print("Invailed choice")
main()