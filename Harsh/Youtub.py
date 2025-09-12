
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from tkinter import *

con = pymysql.connect(
    host="localhost",
    user="root",
    password="Harsh@1901",
    port=3306,
    database="TopsClass"
)

cursor = con.cursor()

root = tk.Tk()
root.geometry("1000x500")
global e1
global e2
global e3
global e4


def Add():
    stuid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    qry = "Insert into record(id,stname,course,fee) values (%s,%s,%s,%s)"
    val = (0,"Harsh","python",44000)
    cursor.execute(qry,val)
    con.commit()
    messagebox.showinfo("information", "Record inserted successfully..")
    for i in Listbox.get_children():
        Listbox.delete(i)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.focus_set()
    show()



def show():
    cursor.execute("select * from record")
    records =cursor.fetchall()
    for i,(id,stname,course,fee) in enumerate (records):
       Listbox.insert("","end",value=(id,stname,course,fee))

def update():
    stuid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    qry = "update Student1 set id=%s,stname=%s,course=%s,fee=%s where id =%s"
    val = (studname,coursename,feee,id)
    cursor.execute(qry,val)
    con.commit()
    for i in Listbox.get_children():
        Listbox.delete(i)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0, END)
    show()



def delete():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0, END)
    show()


tk.Label(root, text="STUDENT REGISTATION", fg="black",font=(None, 30)).place(x=400, y=5)
tk.Label(root, text="Student Id").place(x=10, y=10)
Label(root, text="Student Name").place(x=10, y=40)
Label(root, text="Course").place(x=10, y=70)
Label(root, text="fee").place(x=10, y=100)

e1 =Entry(root)
e1.place(x=140, y=10)

e2 =Entry(root)
e2.place(x=140, y=40)

e3 =Entry(root)
e3.place(x=140, y=70)

e4 =Entry(root)
e4.place(x=140, y=100)


Button(root, text="Add",command= Add,height=3,width=13).place(x=30, y =130)
Button(root, text="Update",command= update,height=3,width=13).place(x=50, y =170)
Button(root, text="delete",command= delete,height=3,width=13).place(x=30, y =200)


cols = ('id','stname','course','fee')
Listbox = ttk.Treeview(root,columns=cols, show='headings')
for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1, column=0, columnspan=2)
    Listbox.place(x=10, y=200)


show() 
# Listbox.bind('<Double-Button-1>',Delete)
root.mainloop()