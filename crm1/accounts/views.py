from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as  sql

# Create your views here.
quantity = 0
payment_info = 0
customer_ID = 0
Delivary_ID = ''
order_name = ''
delivary_id = ''
address = ''
email = ''



def home(request):
    lst = []
    m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
    c = 'SELECT u.first_name, u.last_name, o.o_id FROM users u JOIN order_info o ON u.custid = o.customer_ID'
    #c = "select * from users"
    cursor = m.cursor()
    cursor.execute(c)
    for i in cursor.fetchall():
        lst.append(i)
    
    
    context = {'lst':lst}

    
    return render(request,'accounts/dashboard.html',context)

def products(request):
    created_prod = 0 
    m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
    cursor=m.cursor()

    

    cursor.execute("select * from products")
    prod = []
    
    for i in cursor:
        prod.append(i)
        
    


    return render(request,'accounts/products.html', {'prod': prod})

def users(request):
    #users List
    m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
    cursor=m.cursor()
    cursor.execute("Select * from Users")
    lst = []

    for i in cursor.fetchall():
        lst.append(list(i))
    #Manager List
    manager_lst = []
    cursor.execute("Select * from manager")
    for i in cursor.fetchall():
        manager_lst.append(list(i))
    m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
    cursor=m.cursor()
    cursor.execute("Select * from branch")
    #Branch List
    lst_branch = []
    for i in cursor.fetchall():
        lst_branch.append(list(i))

    #Laundry man
    cursor=m.cursor()
    cursor.execute("Select * from laundryman")

    lst_laundryman = []
    for i in cursor.fetchall():
        lst_laundryman.append(list(i))
    print(lst_laundryman)

    #Delivery man
    cursor=m.cursor()
    cursor.execute("Select * from delivaryman")

    lst_delivaryman = []
    for i in cursor.fetchall():
        lst_delivaryman.append(list(i))

    #Order_info
    cursor=m.cursor()
    cursor.execute("SELECT u.email, o.order_name, o.quantity, o.payment_info, d.name FROM users u INNER JOIN order_info o ON o.customer_id = u.custid INNER JOIN delivaryman d ON o.delivary_id = d.d_id")
    
    lst_orders = []
    for i in cursor.fetchall():
        lst_orders.append(list(i))
    return render(request,'contacts_list_table.html', {'lst':lst, 'manager_lst':manager_lst, 'lst_branch':lst_branch, 'lst_laundryman':lst_laundryman, 'lst_delivaryman':lst_delivaryman, 'lst_orders':lst_orders } )


def customer(request):
    m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
    cursor=m.cursor()
    query = "select First_Name, Last_Name from users"
    cursor.execute(query)
    customer_name = []
    return render(request,'accounts/customer.html')






    
    


    

    

def createOrder(request):
    global quantity,ord_info,customer_ID,order_name, delivary_id, address, payment_info

    

    
    if request.method=="POST":

        mydb=sql.connect(host='localhost',user='root',passwd='',database='crm1')
        mycursor=mydb.cursor()
        dct = request.POST

        for key,value in dct.items():

            if key=="quantity":
                quantity=value
            
            if key=="order_name":
                order_name=value
            if key =="customer_ID":
                customer_ID = value
            if key == 'Regular Wash':
                payment_info = 250*int(quantity)
            elif key == 'Dry Wash':
                payment_info = 400*int(quantity)
            if key == "Delivary_ID":
                delivary_id = value
            if key == "Address":
                address = value 

        query = "INSERT INTO order_info (quantity, payment_info, customer_ID, Delivary_ID, order_name, Address) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (quantity,payment_info,customer_ID,delivary_id,order_name,address)
            
        mycursor.execute(query, val)

        mydb.commit()

        

    context = {}
    return render(request,'accounts/order_form.html', context)
def Add_products(request):
    name = ''
    price = 0
    if request.method=="POST":

        mydb=sql.connect(host='localhost',user='root',passwd='',database='crm1')
        mycursor=mydb.cursor()
        dct = request.POST

        for key,value in dct.items():

            if key=="name":
                name=value
            
            if key=="price":
                price=value
        query = "INSERT INTO products(name,price) VALUES (%s, %s)"
        val = (name,price)
            
        mycursor.execute(query, val)
        mydb.commit()
    context = {}
    return render(request,'accounts/add_products.html', context)


def deleteUser(request):
    global email 
    m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
    cursor=m.cursor()
    cursor.execute("Select * from Users")
    lst = []

    for i in cursor.fetchall():
        lst.append(list(i))
    if request.method=="POST":

        mydb=sql.connect(host='localhost',user='root',passwd='',database='crm1')
        mycursor=mydb.cursor()
        dct = request.POST

        for key,value in dct.items():

            if key=="email":
                email=value
        delete_query = f"DELETE FROM orders WHERE email = {email}"
        
        mycursor.execute(delete_query)
        mydb.commit()

    context = {'lst':lst}
    
    
    



    return render(request,'accounts/delete.html', context)

