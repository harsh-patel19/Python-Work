from tkinter import *
import pymysql

root = Tk()
root.title("Student Management - MYSQL EXAMPLE")
root.geometry("600x500")

Label(root, Text="Name").place(x=50, y=30)
Label(root, text="Email").place(X=50, y=110)
Label(root, text="Phone").place(x=50, y=110)

Entry_name = Entry(root, width=30)
Entry_name.place(x=150, y= 30)

Entry_email = Entry(root, width=30)
Entry_email.place(x=150, y= 70)

Entry_Phone = Entry(root, width=30)
Entry_Phone.place(x=150, y= 110)


cols = ("Id","Name","Email","Phone")

root.mainloop()