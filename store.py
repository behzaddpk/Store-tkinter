from cgitb import html
from tkinter import *
from tkinter import font
from unicodedata import category
import mysql.connector
from mysqlx import Column 
import csv


root = Tk()
root.geometry("700x500")
root.title("Record Data")


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Focus22!",
    database = "record_book",
)


my_cursor = mydb.cursor()
#my_cursor.execute("CREATE DATABASE Record_book")
#Test to show database
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)


'''my_cursor.execute("""CREATE TABLE record(user_id INT AUTO_INCREMENT PRIMARY KEY, 
 \product_name VARCHAR(255), 
 \product_detail VARCHAR(255), 
 \product_category VARCHAR(255),  
 \product_price DECIMAL(10, 2))""")'''



'''#to add coulmn in table
#my_cursor.execute("ALTER TABLE record Add")
 \product_name VARCHAR(255), 
 \product_detail VARCHAR(255), 
 \product_category VARCHAR(255),  
 \product_price DECIMAL(10, 2))")'''

'''#for print record
my_cursor.execute("SELECT * FROM record")
#print(my_cursor.description)

for thing in my_cursor.description:
    print(thing)'''

def update():
    sql_command = "UPDATE record SET product_name = %s, product_detail = %s, product_category = %s, product_price = %s WHERE product_id = %s"

    
    name = products_name.get()
    detail = products_detail.get()
    category = products_category.get()
    price = products_price.get()

    id_value = box.get()
    inputs = (name, detail, category, price, id_value)
    my_cursor.execute(sql_command, inputs)
    mydb.commit()


    update_record.destroy()
    


def edit():
    global update_record
    update_record = Tk()
    update_record.geometry("500x300")

    record_id = box.get()
    my_cursor.execute("SELECT * FROM record WHERE product_id = " + record_id)
    records = my_cursor.fetchall()


    global products_name
    global products_detail
    global products_category
    global products_price



    products_name = Entry(update_record, width=30)
    products_name.grid(row=0, column=1, padx=20)
    products_detail = Entry(update_record, width=30)
    products_detail.grid(row=1, column=1, padx=20)
    products_category = Entry(update_record, width=30)
    products_category.grid(row=2, column=1, padx=20)
    products_price = Entry(update_record, width=30)
    products_price.grid(row=3, column=1, padx=20)


    products_name_label = Label(update_record, text="Product Name").grid(row=0, column=0)
    products_detail_lable = Label(update_record, text="product detatail")
    products_detail_lable.grid(row=1, column=0)
    products_category_lable = Label(update_record, text="product category")
    products_category_lable.grid(row=2, column=0)
    products_price_lable = Label(update_record, text="product price")
    products_price_lable.grid(row=3, column=0)

    for record in records:
        products_name.insert(0, record[1])
        products_detail.insert(0, record[2])
        products_category.insert(0, record[3])
        products_price.insert(0, record[4])


    edit_btn = Button(update_record, text="Save record", command=update)
    edit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=168)



def delete():
    searched = box.get()
    sql = "DELETE FROM record WHERE product_id = %s"
    name = (searched, )
    result = my_cursor.execute(sql, name)
    mydb.commit()
    print(result)




def search():
    search_record = Tk()
    search_record.title("Search Data")
    search_record.geometry("500x400")

    searched = box.get()
    sql = "SELECT * FROM record WHERE product_id = %s"
    name = (searched, )
    result = my_cursor.execute(sql, name)
    result = my_cursor.fetchall()

    if not result:
        result = "Record not found..."

    for index, result in enumerate(result):
        num = 0
        for final_result in result:
            record_label = Label(search_record, text=final_result)
            record_label.grid(row=index, column=num, padx=8, pady=8)
            num +=1

def query():
    list_record = Tk()
    list_record.title("Record Data")
    list_record.geometry("500x400")

    my_cursor.execute("SELECT * FROM record")
    results = my_cursor.fetchall()
    for index, result in enumerate(results):
        num = 0
        for final_result in result:
            record_label = Label(list_record, text=final_result)
            record_label.grid(row=index, column=num, padx=8, pady=8)
            num +=1

    

def submit():
    sql_command = "INSERT INTO record (product_name, product_detail, product_category, product_price) VALUES (%s, %s, %s, %s)"
    values = (prod_name.get(), prod_discpt.get(), prod_catgory.get(), prod_price.get())
    my_cursor.execute(sql_command, values)

    mydb.commit()

    prod_name.delete(0, END)
    prod_discpt.delete(0, END)
    prod_catgory.delete(0, END)
    prod_price.delete(0, END)

def logout():
    root.destroy()
    import index


logout_btn = Button(root, width=10, height=2, text="Logout", font=('Normal', 10, 'bold'), command=logout)
logout_btn.place(x=580, y=50)

title = Label(root, text="Recorded Data", font=('Arial', 35, 'bold')).place(x=130, y=30)
prod_name_lable = Label(root, text="Product Name:", font=('Arial', 10, 'bold'))
prod_name_lable.place(x=120, y=110)
prod_discpt_lable = Label(root, text="Product Discription: ", font=('Arial', 10, 'bold'))
prod_discpt_lable.place(x=120, y=135)
prod_catgory_lable = Label(root, text="Product Category: ", font=('Arial', 10, 'bold'))
prod_catgory_lable.place(x=120, y=160)
prod_price_lable = Label(root, text="Product Price: ", font=('Arial', 10, 'bold'))
prod_price_lable.place(x=120, y=185)
box_label = Label(root, text="Select Id: ", font=('Arial', 10, 'bold'))
box_label.place(x=120, y=330)


prod_name = Entry(root, width=35)
prod_name.place(x=270, y=110)
prod_discpt = Entry(root, width=35)
prod_discpt.place(x=270, y=135)
prod_catgory = Entry(root, width=35)
prod_catgory.place(x=270, y=160)
prod_price = Entry(root, width=35)
prod_price.place(x=270, y=185)
box = Entry(root, width=35)
box.place(x=270, y=330)



submit_btn = Button(root, text="Add Record to Database", command=submit, font=('Arial', 10, 'bold'), width= 40)
submit_btn.place(x=140, y=220)

query_btn = Button(root, text="show record", command=query, font=('Arial', 10, 'bold'), width= 40)
query_btn.place(x=140, y=270)

delete_btn = Button(root, text="Delete record", command=delete, width=20, font=('Arial', 10, 'bold'))
delete_btn.place(x=100, y=370)

search_btn = Button(root, text="Search record", command=search, width=20, font=('Arial', 10, 'bold'))
search_btn.place(x=300, y=370)

edit_btn = Button(root, text="Edit record", command=edit, width=20, font=('Arial', 10, 'bold'))
edit_btn.place(x=180, y=425)


root.mainloop()