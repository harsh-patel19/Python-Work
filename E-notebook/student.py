
choice =0
student = {}
while(choice!=4):
    print("""
        *WELCOME TO STUDENTS MANAGEMENTS*
        press 1 for add student
        press 2 for view deatils
        press 3 for delete
        press 4 for exit
    """)

    choice = int(input("enter choice : "))
    if choice ==1:
        print("adding the student")
        name = input("enter the name please: ")
        lastname = input("enter the lastname please: ")
        email = input("enter the email please: ")
        student.update({name:{"lastname":lastname,"email":email}})
        
    elif choice ==2:
        print("view students")
        print(student)
    elif choice ==3:
        print("delete")
        student.clear
    elif choice ==4:
        print("exit the programm")
    else:
        print("INvaild choice..")