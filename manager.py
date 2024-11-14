from ast import Delete
from tkinter import *
from tkinter.tix import INTEGER
import mysql.connector
from tkinter import messagebox


manager = Tk()
manager.geometry("700x500")
manager.title("Add Manager")


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Focus22!",
    database = "record_book",
    )
my_cursor = mydb.cursor()


def submit_salesman_logout():
    salesman_reg.destroy()
    import index

def register_salesman():
    global salesman_reg
    manager_frame.destroy()
    salesman_reg = Tk()
    salesman_reg.geometry("700x500")
    salesman_reg.title("Add Guard")

    

    def submit_salesman():
        sql_command = "INSERT INTO user (username, email, address, phone_no, password) VALUES (%s, %s, %s, %s, %s)"
        values = (username.get(), email.get(), address.get(), phoneno.get(), password.get())
        my_cursor.execute(sql_command, values)
        mydb.commit()


        if(my_cursor.execute(sql_command, values)):
            messagebox.showinfo('alert','New SalesMan is now Registerd')
        else:
            messagebox.showinfo('alert','New SalesMan is now Registerd')

        userr_name.delete(0,END)
        mail.delete(0,END)
        addresses.delete(0,END)
        contact.delete(0,END)
        passwrd.delete(0,END)


    username = StringVar()
    email = StringVar()
    address = StringVar()
    phoneno = StringVar()
    password = StringVar()

    logout_btn = Button(salesman_reg, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=submit_salesman_logout)
    logout_btn.place(x=580, y=50)


    
    Label(salesman_reg, text="SalesMan Registration Page", font=('Uchen', 20, 'bold')).place(x=170, y=50)

    Label(salesman_reg, text="User Name: ",font=('Normal', 10, 'bold') ).place(x=150, y=150)
    userr_name = Entry(salesman_reg, width=25, textvariable=username)
    userr_name.place(x=250, y=150)
    Label(salesman_reg, text="Email: ",font=('Normal', 10, 'bold') ).place(x=150, y=200)
    mail = Entry(salesman_reg, width=25, textvariable=email)
    mail.place(x=250, y=200)
    Label(salesman_reg, text="Address: ",font=('Normal', 10, 'bold') ).place(x=150, y=250)
    addresses = Entry(salesman_reg, width=25, textvariable=address)
    addresses.place(x=250, y=250)
    Label(salesman_reg, text="Phone No: ",font=('Normal', 10, 'bold') ).place(x=150, y=300)
    contact = Entry(salesman_reg, width=25, textvariable=phoneno)
    contact.place(x=250, y=300)
    Label(salesman_reg, text="Password: ",font=('Normal', 10, 'bold') ).place(x=150, y=350)
    passwrd= Entry(salesman_reg, width=25, textvariable=password, show="*")
    passwrd.place(x=250, y=350)
    Button(salesman_reg, text="Submit", relief="groove", width=25, font=('arial', 12, 'bold'),command=submit_salesman).place(x=150, y=400)


def manage_salesman():
    global view_salesman
    manager_frame.destroy()
    view_salesman = Tk()
    view_salesman.geometry("700x500")
    view_salesman.title("Guard Frame")

    def manage_salesman_logout():
        view_salesman.destroy()
        import index

    logout_btn = Button(view_salesman, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=manage_salesman_logout)
    logout_btn.place(x=580, y=50)

    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchall()
    for index, result in enumerate(results):
        num = 0
        for final_result in result:
            record_label = Label(view_salesman, text=final_result)
            record_label.grid(row=index, column=num, padx=8, pady=8)
            num +=1



def manager_frame():
    global manager_frame
    manager.destroy()
    manager_frame = Tk()
    manager_frame.geometry("700x500")
    manager_frame.title("Manager Frame")

    def manger_frame_logout():
        manager_frame.destroy()
        import index

    logout_btn = Button(manager_frame, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=manger_frame_logout)
    logout_btn.place(x=580, y=50)

    admin_btn = Button(manager_frame, width=15, height=4, text="Manage SalesMan", font=('Uchen', 10, 'bold'), command=manage_salesman)
    admin_btn.place(x=150, y=180)

    admin_btn = Button(manager_frame, width=15, height=4, text="Register SalesMan", font=('Uchen', 10, 'bold'), command=register_salesman)
    admin_btn.place(x=400, y=180)


def login_verification():
    my_cursor.execute('select user_name , password from manager')
    total = my_cursor.fetchall()
    user_name = username.get()
    passwrd = password.get()
    for i in total:
        if user_name == i[0] and passwrd == i[1]:
            manager_frame()
        elif user_name == i[0] and passwrd != i[1]:
            messagebox.showinfo('ALERT!', 'Enter Correct Password')
            break
    
        
        

Label(manager, text="Manager Login Page", font=('Uchen', 20, 'bold')).place(x=170, y=50)

global username_verification
global password_verification
global e1
global e2
username = StringVar()
password = StringVar()
Label(manager, text="").pack()
Label(manager, text="Username :", fg="black", font=('arial', 12, 'bold')).place(x=150, y=150)
e1=Entry(manager, textvariable=username, width=25).place(x=260, y=150)
Label(manager, text="Password :", fg="black", font=('arial', 12, 'bold')).place(x=150, y=200)
e2=Entry(manager, textvariable=password, width=25, show="*").place(x=260, y=200)
Button(manager, text="Login", relief="groove", width=26, font=('arial', 12, 'bold'),command=login_verification).place(x=150, y=250)


manager.mainloop()