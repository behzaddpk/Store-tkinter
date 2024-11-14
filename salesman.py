from ast import Delete, Store
from tkinter import *
from tkinter.tix import INTEGER
import mysql.connector
from tkinter import messagebox



global salesman
salesman = Tk()
salesman.geometry("700x500")
salesman.title("SalesMan Login Page")


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Focus22!",
    database = "record_book",
    )
my_cursor = mydb.cursor()



def store_frame():
    salesman.destroy()
    import store
    



def login_verification():
    my_cursor.execute('select username , password from user')
    total = my_cursor.fetchall()
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    for i in total:
        if user_verification == i[0] and pass_verification == i[1]:
            store_frame()

        elif user_verification == i[0] and pass_verification != i[1]:
                messagebox.showinfo('ALERT!', 'Enter Correct Password')
                break
            

Label(salesman, text="SalesMan Login Page", font=('Uchen', 20, 'bold')).place(x=170, y=50)

global username_verification
global password_verification
global e1
global e2
username_verification = StringVar()
password_verification = StringVar()
Label(salesman, text="").pack()
Label(salesman, text="Username :", fg="black", font=('arial', 12, 'bold')).place(x=150, y=150)
e1=Entry(salesman, textvariable=username_verification, width=25).place(x=260, y=150)
Label(salesman, text="Password :", fg="black", font=('arial', 12, 'bold')).place(x=150, y=200)
e2=Entry(salesman, textvariable=password_verification, width=25, show="*").place(x=260, y=200)
Button(salesman, text="Login", relief="groove", width=26, font=('arial', 12, 'bold'),command=login_verification).place(x=150, y=250)


salesman.mainloop()