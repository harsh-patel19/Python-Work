choice =0
enotes = {}
while(choice!=4):
        print( """
            WELCOME TO PYHTON E - note...
            press 1 for generate note
            press 2 for view note
            press 4 for exit
        """)
        choice = int(input("enter choice : "))
        if choice ==1:
            print("-----------genertae notes----------")
            name = input("enter name: ")
            title = input("enter title: ")
            content =input("enter content: ")
            enotes.update({name:{"title":title,"content":content}})

        elif choice ==2:
            print("-------view notes-----")
            print(enotes)

        elif choice ==4:
            print("----Exit---")
        else:
            print("Invaild input")