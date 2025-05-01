from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(host='localhost',database='e_bike_rental',user='root',password='')
cursor=conn.cursor()

# cursor.execute("create table department (id primary key, name varchar(20))")

def getdata():
    cursor=conn.cursor()
    cursor.execute("select * from ebike")
    x=cursor.fetchall()
    return x

def updatedata(id,brand,model,battery,price):
    cursor = conn.cursor()
    data = (brand,model,battery,price,id)
    query = "UPDATE ebike SET brand = %s, model = %s, battery = %s, price = %s WHERE id = %s;" 
    cursor.execute(query, data)
    conn.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False
    
def deletedata(id):
    cursor = conn.cursor()
    data = (id,)
    query = "delete from ebike where id=%s" 
    cursor.execute(query, data)
    conn.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False
    
def insertdata(id,brand,model,battery,price):
    try:
        cursor = conn.cursor()
        data = (id,brand,model,battery,price)
        query = "INSERT INTO ebike (id, brand, model, battery, price) VALUES (%s,%s,%s,%s,%s);"
        cursor.execute(query, data)
        conn.commit()
        return True
    except:
        return False



def insertwindow(window):
    window.destroy()
    insert=Tk()
    insert.geometry("250x250")
    insert.title("Insert New Data")
    

    idLabel=Label(insert,text="ID : ")
    idLabel.place(x=50,y=30)
    id=Entry(insert)
    id.place(x=80,y=30)
    
    brandLabel=Label(insert,text="Brand : ")
    brandLabel.place(x=30,y=60)
    brand=Entry(insert)
    brand.place(x=80,y=60)
    
    modelLabel=Label(insert,text="Model : ")
    modelLabel.place(x=30,y=90)
    model=Entry(insert)
    model.place(x=80,y=90)
    
    batteryLabel=Label(insert,text="Battery : ")
    batteryLabel.place(x=30,y=120)
    battery=Entry(insert)
    battery.place(x=80,y=120)
    
    priceLabel=Label(insert,text="Price : ")
    priceLabel.place(x=40,y=150)
    price=Entry(insert)
    price.place(x=80,y=150)

    def insertFun():
        i=id.get()
        b=brand.get()
        m=model.get()
        ba=battery.get()
        p=price.get()

        x=insertdata(i,b,m,ba,p)
        
        if x:
            insert.destroy()
        else:
            messagebox.showerror("Error", "Id Already Exists")

    
    btn=Button(insert,text="Submit",command=insertFun)
    btn.place(x=100,y=175)

    insert.mainloop()


def updatewindow(window):
    window.destroy()
    update=Tk()
    update.geometry("250x250")
    update.title("Update Data")

    idLabel=Label(update,text="ID : ")
    idLabel.place(x=50,y=30)
    id=Entry(update)
    id.place(x=80,y=30)
    
    brandLabel=Label(update,text="Brand : ")
    brandLabel.place(x=30,y=60)
    brand=Entry(update)
    brand.place(x=80,y=60)

    modelLabel=Label(update,text="Model : ")
    modelLabel.place(x=30,y=90)
    model=Entry(update)
    model.place(x=80,y=90)
    
    batteryLabel=Label(update,text="Battery : ")
    batteryLabel.place(x=30,y=120)
    battery=Entry(update)
    battery.place(x=80,y=120)

    priceLabel=Label(update,text="Price : ")
    priceLabel.place(x=40,y=150)
    price=Entry(update)
    price.place(x=80,y=150)
    
    
    def updateFun():
        i=id.get()
        b=brand.get()
        m=model.get()
        ba=battery.get()
        p=price.get()

        x=updatedata(i,b,m,ba,p)
        if x:
            update.destroy()
        else:
            messagebox.showerror("Error", "Id No Id Found")
    
    btn=Button(update,text="Submit",command=updateFun)
    btn.place(x=100,y=175)

    update.mainloop()


def deletewindow(window):
    window.destroy()
    delete=Tk()
    delete.geometry("300x200")
    delete.title("Delete Data")
    

    idLabel=Label(delete,text="ID : ")
    idLabel.place(x=50,y=30)
    id=Entry(delete)
    id.place(x=80,y=30)
    
    def deleteFun():
        i=id.get()
        x=deletedata(i)
        if x:
            delete.destroy()
        else:
            messagebox.showerror("Error", "Id Not Found")
    
    btn=Button(delete,text="Submit",command=deleteFun)
    btn.place(x=100,y=120)
    delete.mainloop()



def mainwindow():

    window=Tk()

    window.geometry("550x500")
    window.title("E BIKE MANAGEMENT")

    title=Label(window,text="E BIKE MANAGEMENT",font=("Comic Sans MS", 25),fg="green")
    title.place(x=80,y=30)
    
    def deletefun():
        deletewindow(window)
        mainwindow()

    def updatefun():
        updatewindow(window)
        mainwindow()

    def insertfun():
        insertwindow(window)
        mainwindow()

    insertbtn=Button(text="Insert Data",font=("Comic Sans MS", 15),command=insertfun)
    insertbtn.place(x=50,y=100)

    updatebtn=Button(text="Update Data",font=("Comic Sans MS", 15),command=updatefun)
    updatebtn.place(x=200,y=100)
        

    deletebtn=Button(text="Delete Data",font=("Comic Sans MS", 15),command=deletefun)
    deletebtn.place(x=350,y=100)


    labelframe=LabelFrame(window,text="E Bikes Table",font=("Comic Sans MS", 10),fg="blue")
    labelframe.place(x=100,y=180)

    heading1=Label(labelframe,text="Bike ID")
    heading1.grid(row=0,column=0,padx=10,pady=10)

    heading2=Label(labelframe,text="Brand")
    heading2.grid(row=0,column=1,padx=10,pady=10)

    heading3=Label(labelframe,text="Model")
    heading3.grid(row=0,column=2,padx=10,pady=10)

    heading4=Label(labelframe,text="Battery")
    heading4.grid(row=0,column=3,padx=10,pady=10)

    heading5=Label(labelframe,text="Price")
    heading5.grid(row=0,column=4,padx=10,pady=10)

    x=getdata()

    for i in range(0,len(x)):
        data1=Label(labelframe,text=x[i][0])
        data1.grid(row=i+1,column=0,padx=10,pady=10)
        data2=Label(labelframe,text=x[i][1])
        data2.grid(row=i+1,column=1,padx=10,pady=10)
        data3=Label(labelframe,text=x[i][2])
        data3.grid(row=i+1,column=2,padx=10,pady=10)
        data4=Label(labelframe,text=x[i][3])
        data4.grid(row=i+1,column=3,padx=10,pady=10)
        data5=Label(labelframe,text=x[i][4])
        data5.grid(row=i+1,column=4,padx=10,pady=10)

    window.mainloop()

mainwindow()
