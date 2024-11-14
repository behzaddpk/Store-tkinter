from tkinter import *
# import mysql.connector
from tkinter import messagebox
import sqlite3



conn = sqlite3.connect('store_book.db')
my_cursor = conn.cursor()

#my_cursor.execute("CREATE TABLE register(user_id INT AUTO_INCREMENT PRIMARY KEY,  name VARCHAR(255), username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")



root = Tk()
root.geometry("700x550")
root.title("Registration Page")

def submit():

    conn = sqlite3.connect('store_book.db')
    my_cursor = conn.cursor()
    name = t1.get()
    user_name = t2.get()
    email = t3.get()
    passwrd = t4.get()

    sql_command = "INSERT INTO register (name, username, email, password) VALUES (%s, %s, %s, %s)"
    values = (name, user_name, email, passwrd)
    my_cursor.execute(sql_command, values)
    my_cursor.commit()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

    conn.commit()
    conn.close()

'''    if name and user_name and email and passwrd and cpasswrd:
        my_cursor.execute("SELECT username, email from register")
        total = my_cursor.fetchall()
        username = []
        exist_email = []
        for i in total:
            username.append(i[0])
            exist_email.append(i[0])
        
        if email in exist_email:
            messagebox.showinfo('Alert!', "Email is already exist")
            e3.delete(0,END)
        else:
            if passwrd == cpasswrd:
                my_cursor.execute(f'insert into register values("{name}";"{user_name}","{email}","{passwrd}")') 
                
                mydb.commit()
                messagebox.showinfo('Success!', "Registration Completed")
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)


    else: 
        messagebox.showinfo('Alert!', "All fields are must be filled")'''

l0 = Label(root, text = "Registration Page", font=('normal', 25, 'bold'))
l0.place(x=170, y=40)

l1 = Label(root, text = "Name: ", font=('normal', 10, 'bold'))
l1.place(x=150, y=120)

l2 = Label(root, text = "User Name: ", font=('normal', 10, 'bold'))
l2.place(x=150, y=160)

l3 = Label(root, text = "Email Address: ", font=('normal', 10, 'bold'))
l3.place(x=150, y=200)

l4 = Label(root, text = "Password: ", font=('normal', 10, 'bold'))
l4.place(x=150, y=240)


t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()

e1 = Entry(root, width=30, textvariable=t1)
e1.place(x=280, y=120)

e2 = Entry(root, width=30, textvariable=t2)
e2.place(x=280, y=160)

e3 = Entry(root, width=30, textvariable=t3)
e3.place(x=280, y=200)

e4 = Entry(root, width=30, textvariable=t4, show="*")
e4.place(x=280, y=240)


b1 = Button(root, width=30, text="Submit", command=submit, font=('normal', 12, 'bold'))
b1.place(x=155, y=280)


conn.commit()
conn.close()
root.mainloop()