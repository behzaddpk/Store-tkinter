from ast import Delete
from glob import glob
from tkinter import Tk
from tkinter import *
from operator import index
from tkinter.tix import INTEGER
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Focus22!",
    database = "record_book",
)

my_cursor = mydb.cursor()


global main
main = Tk()
main.geometry("700x500")
main.title("Login Pages")



#admin Frame Coding

def manager_register():
    global mang_reg
    admin_frame.destroy()
    mang_reg = Tk()
    mang_reg.geometry("700x500")
    mang_reg.title("Add Manager")

    def mang_reg_logout():
        mang_reg.destroy()
        import index    

    def submit_mang():
        sql_command = "INSERT INTO manager (user_name, email, address, phone_no, password) VALUES (%s, %s, %s, %s, %s)"
        values = (username.get(), email.get(), address.get(), phoneno.get(), password.get())
        my_cursor.execute(sql_command, values)
        mydb.commit()


        if(my_cursor.execute(sql_command, values)):
            messagebox.showinfo('alert','New Manager is now Registerd')
        else:
            messagebox.showinfo('alert','New Manager is now Registerd')

       
        userr_name.delete(0,END)
        mail.delete(0,END)
        addresses.delete(0,END)
        contact.delete(0,END)
        passwrd.delete(0,END)

    logout_btn = Button(mang_reg, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=mang_reg_logout)
    logout_btn.place(x=580, y=50)
    Label(mang_reg, text="Register New Manager", font=('Uchen', 20, 'bold')).place(x=170, y=50)

    username = StringVar()
    email = StringVar()
    address = StringVar()
    phoneno = StringVar()
    password = StringVar()

    

    Label(mang_reg, text="User Name: ",font=('Normal', 10, 'bold') ).place(x=150, y=150)
    userr_name = Entry(mang_reg, width=25, textvariable=username)
    userr_name.place(x=250, y=150)
    Label(mang_reg, text="Email: ",font=('Normal', 10, 'bold') ).place(x=150, y=200)
    mail = Entry(mang_reg, width=25, textvariable=email)
    mail.place(x=250, y=200)
    Label(mang_reg, text="Address: ",font=('Normal', 10, 'bold') ).place(x=150, y=250)
    addresses = Entry(mang_reg, width=25, textvariable=address)
    addresses.place(x=250, y=250)
    Label(mang_reg, text="Phone No: ",font=('Normal', 10, 'bold') ).place(x=150, y=300)
    contact = Entry(mang_reg, width=25, textvariable=phoneno)
    contact.place(x=250, y=300)
    Label(mang_reg, text="Password: ",font=('Normal', 10, 'bold') ).place(x=150, y=350)
    passwrd= Entry(mang_reg, width=25, textvariable=password, show="*")
    passwrd.place(x=250, y=350)
    Button(mang_reg, text="Submit", relief="groove", width=25, font=('arial', 12, 'bold'),command=submit_mang).place(x=150, y=400)
    


def manag_frame_logout():
    manag_frame.destroy()
    import index    


def backwardbtn():
    mang_reg.destroy()
    admin_frame()

def manage_manager():
    admin_frame.destroy()
    global manag_frame
    manag_frame = Tk()
    manag_frame.geometry("700x500")
    manag_frame.title("Manager Frame")


    my_cursor.execute("SELECT * FROM manager")
    results = my_cursor.fetchall()
    for index, result in enumerate(results):
        num = 0
        for final_result in result:
            record_label = Label(manag_frame, text=final_result)
            record_label.grid(row=index, column=num, padx=8, pady=8)
            num +=1
    
    logout_btn = Button(manag_frame, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=manag_frame_logout)
    logout_btn.place(x=580, y=50)

   

def admin_frame_logout():
    admin_frame.destroy()
    import index

def admin_frame():
    admin.destroy()
    global admin_frame
    admin_frame = Tk()
    admin_frame.geometry("700x500")
    admin_frame.title("Admin Frame")

    logout_btn = Button(admin_frame, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=admin_frame_logout)
    logout_btn.place(x=580, y=50)
    admin_btn = Button(admin_frame, width=15, height=4, text="Manage Managerr", font=('Uchen', 10, 'bold'), command=manage_manager)
    admin_btn.place(x=150, y=180)

    admin_btn = Button(admin_frame, width=15, height=4, text="Add Manager", font=('Uchen', 10, 'bold'), command=manager_register)
    admin_btn.place(x=400, y=180)
    

      




def admin():
    main.destroy()
    global admin
    admin = Tk()
    admin.geometry("700x500")
    admin.title("Login Pages")
    


    def login_verification():
        my_cursor.execute('select username , password from register')
        total = my_cursor.fetchall()
        user_verification = username_verification.get()
        pass_verification = password_verification.get()
        for i in total:
            if user_verification == i[0] and pass_verification == i[1]:
                admin_frame()

            elif user_verification == i[0] and pass_verification != i[1]:
                    messagebox.showinfo('ALERT!', 'Enter Correct Password')
                    break
        
            else:
                messagebox.showinfo('ALERT!', 'User Not Registered')
    
    
            
    Label(admin, text="Admin Login Page", font=('Uchen', 20, 'bold')).place(x=170, y=50)

    global username_verification
    global password_verification
    global e1
    global e2
    username_verification = StringVar()
    password_verification = StringVar()
    Label(admin, text="Username :", fg="black", font=('arial', 12, 'bold')).place(x=150, y=150)
    e1=Entry(admin, textvariable=username_verification, width=25).place(x=260, y=150)
    Label(admin, text="Password :", fg="black", font=('arial', 12, 'bold')).place(x=150, y=200)
    e2=Entry(admin, textvariable=password_verification, width=25, show="*").place(x=260, y=200)
    Button(admin, text="Login", relief="groove", width=26, font=('arial', 12, 'bold'),command=login_verification).place(x=150, y=250)






#manager Frame Coding

def manager_panel():
    main.destroy()
    import manager

#SalesMan Frame Coding
def sales_man():
    main.destroy()
    import salesman

def admin_registration():
    main.destroy()
    import Register




#Index frame coding
Label(main, text="Login Pages", font=('Uchen', 20, 'bold')).place(x=250, y=50)

admin_btn = Button(main, width=15, height=4, text="Login As Admin", font=('Uchen', 10, 'bold'), command=admin)
admin_btn.place(x=150, y=180)

admin_btn = Button(main, width=15, height=4, text="Login As Manager", font=('Uchen', 10, 'bold'), command=manager_panel)
admin_btn.place(x=400, y=180)

admin_btn = Button(main, width=15, height=4, text="Login As SalesMan", font=('Uchen', 10, 'bold'), command=sales_man)
admin_btn.place(x=280, y=340)


admin_btn = Button(main, width=15, height=4, text="Add New Admin", font=('Uchen', 5, 'bold'), command=admin_registration)
admin_btn.place(x=600, y=440) 
main.mainloop()