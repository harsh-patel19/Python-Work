
from tkinter import *
from tkinter import ttk, messagebox
import pymysql

# ------- DB connection ---------

con = pymysql.connect(
    host="localhost",
    user="root",
    password="Harsh@1901",
    port= 3306,
    database= "inventory_db"
)

cursor = con.cursor()

root = Tk()
root.geometry("1000x700")
root.title("------PRODUCT INVENTORY MANAGER------")


#  ------- Functions --------

def add_product():
    name  = t1.get()
    price = t2.get()
    qty   = t3.get()
    if name == "" or price == "" or qty == "":
        messagebox.showerror("Error", "All fields are required")
        return
    qry = "Insert into products values (%s,%s,%s,%s)"
    val = (0, name, price,qty)
    cursor.execute(qry,val)
    con.commit()    
    clear_fields()
    refresh_table()
    messagebox.showinfo("sucess", "Product added!")


def refresh_table():
    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()
    for i in table.get_children():
        table.delete(i)
    for r in records:
        table.insert("","end",values=r)


def get_data(event):
    global selected_id
    row = table.selection()[0]
    data = table.item(row)['values']
    selected_id = data[0]
    clear_fields()
    t1.insert(0, data[1])
    t2.insert(0, data[2])
    t3.insert(0, data[3])

def update_product():
    if not selected_id:
        messagebox.showerror("error", "select a product to update ")
        return
    name, price, qty = t1.get(), t2.get(), t3.get()
    qry = "UPDATE products set name=%s, price=%s, quantity=%s where id =%s"
    val = (name, price, qty, selected_id)
    cursor.execute(qry, val)
    con.commit()
    clear_fields()
    refresh_table()
    messagebox.showinfo("success","Product updated!")

def delete_product():
    if not selected_id:
        messagebox.showerror("error","select a product to delete")
        return
    cursor.execute("DELETE FROM products where id =%s", (selected_id ,))
    con.commit()
    clear_fields()
    refresh_table()
    messagebox.showinfo("sucess","Product deleted!")



def clear_fields():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)



Label(root, text="Product Name").place(x=100,y=100)
Label(root, text="Price").place(x=100,y=150)
Label(root, text="Quantitly").place(x=100, y=200)

t1 = Entry(root)
t1.place(x=200, y=100)
t2 = Entry(root)
t2.place(x=200, y=150)
t3 = Entry(root)
t3.place(x=200, y=200)


Button(root, text="Add",width=15,command=add_product).place(x=200, y=250)
Button(root, text="update",width=15,command=update_product).place(x=300, y=250)
Button(root, text="delete",width=15,command=delete_product).place(x=400, y=250)
Button(root, text="clear",width=15,command=clear_fields).place(x=500, y=250)

cols =("Id","Name","Price","Quantity")
table =ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col)
    table.column(col, width=150)
table.place(x=50, y=320, width=800, height=300)

table.bind("<Double-1>", get_data)

selected_id =None
refresh_table()

root.mainloop()


