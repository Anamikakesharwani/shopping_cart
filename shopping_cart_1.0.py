import pymysql
import hashlib
from tabulate import tabulate



class user:
    def get_connection():
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="shopping_cart" )
        cursor = connection.cursor()
        return cursor
    

    def authentication():
        print("Welcome to Shopping Cart\n")
        
        while True:
            ch=int(input("Choose option below\nPress 1 for Login\nPress 2 for Register\nPress 3  for logout\n"))
            if ch is 1:
                    name = input("Enter the username \n")
                    password=input("enter the password \n")
                    m=hashlib.md5()
                    m.update(password.encode("utf-8"))
                    pwd=m.hexdigest()

                    #database connection
                    cursor=user.get_connection()
                    sql = "select * from users where username = %s AND password = %s"
                    param=(name,pwd,)
                    cursor.execute(sql, param)
                    result=cursor.fetchall()
                    #print(result)
                    global current_user_id,current_user,current_usertype
                    current_user_id = result[0][0]
                    current_user = result[0][1]
                    current_usertype = result[0][3]
                    cursor.close()

                    if current_usertype == 0:
                        Admin.operation()
                    else:
                        Customer.customer_operation()

            elif ch is 2: 
                    connection = pymysql.connect(host="localhost",user="root",passwd="",database="shopping_cart" )
                    cursor = connection.cursor()
                    name = input("Enter the username \n")
                    password=input("Enter the password \n")
                    m=hashlib.md5()
                    m.update(password.encode("utf-8"))
                    pwd=m.hexdigest()
                    
                    insert_query = "insert into users (username,password) values (%s, %s)"
                    param=(name,pwd)
                    cursor.execute(insert_query,param)
                    connection.commit()
                    cursor.close()
                    db.close()
                    print("Registration Successful\n Please Login")
            elif ch is 3:
                exit()
            else:    
                    print("Invalid Option Selected,")    
        
        

class Admin:
    def operation():
        while True:
            print("1.Add new Product\n2.Delete existing product\n3.Browse all products\n4.Exit\n")
        
            userchoice = int(input("Select the option:\n"))
            if userchoice is 1:
                Admin.add_product()
            elif userchoice is 2:
                Admin.delete_product()
            elif userchoice is 3:
                Admin.browse_product()
            elif userchoice is 4:
                exit()
            else:
                print("invalid selection ")
    
    def add_product():
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="shopping_cart" )
        cursor = connection.cursor()
        title = input("enter the product name\n")
        price = input("enter the product price\n")
        qnty = input("enter the product quantity\n")
        mySql_insert_query = " INSERT INTO products (title,price,qty)  VALUES ( %s, %s, %s) "
        recordTuple = (title, price, qnty)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into table")
        cursor.close()
        connection.close()

    def delete_product():
        cursor=user.get_connection()
        all_product="select * from products"
        cursor.execute(all_product)
        records = cursor.fetchall()
        print(records)
        for row in records:
            print("Product_Id = ", row[0], )
            print("Name = ", row[1])
            print("Price  = ", row[2])
            print("Quantity = ", row[3], "\n")
        productid=int(input("enter the productid for deletion\n"))
        sql_Delete_query = "Delete from products where productid = %s"
        param = (productid,)
        cursor.execute(sql_Delete_query,param)
        print("Deletion Successfull")
        cursor.close

    def browse_product():
        cursor=user.get_connection()
        all_product="select * from products"
        cursor.execute(all_product)
        records = cursor.fetchall()
        for row in records:
            print("product_Id = ", row[0], )
            print("Name = ", row[1])
            print("Price  = ", row[2])
            print("Quantity = ", row[3], "\n")

class Customer():
    def customer_operation():
        while True:
            print("Select an option:\n")
            print("1.Add Products to Cart\n2.View Cart\n3.Remove from cart\n4.exit")
            userchoice = int(input("enter your choice\n"))
            if userchoice is 1:
                Customer.browse_product()
                Customer.add_to_cart()
            elif userchoice is 2:
                Customer.view_cart()
            elif userchoice is 3:
                Customer.remove_from_cart()
            elif userchoice is 4:
                exit()
            else:
                print("invalid selection, please choose again\n")


    def browse_product():
        cursor=user.get_connection()
        all_product="select productid, title, price, qty from products where qty > 0"
        cursor.execute(all_product)
        records = cursor.fetchall()
        print(tabulate(records, headers=['ProductID', 'title', 'Price', 'Stock'], tablefmt='psql'))
        cursor.close()
        
    def add_to_cart():
        global current_user_id
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="shopping_cart" )
        cursor = connection.cursor()
        product_id = input("Enter comma seperated product_id for purchasing\n")
        pids = product_id.split(',')
        cart_id = None
        query=("select cartid from cart where userid=%s")
        para=(current_user_id)
        cursor.execute(query,para)
        query = None
        if cart_id is None:
        	query = "insert into cart (cart_total,userid) values (%s,%s)"
        else:
        	query = "update cart set cart_total = %s where userid = %s"
        
        param=(0,current_user_id)
        cursor.execute(query,param)
        connection.commit()
        cartid = cursor.lastrowid
        for products in pids:
            query = "insert into cart_products (productid,cartid) values (%s,%s)"
            param=(products, cartid)
            cursor.execute(query,param)
            connection.commit()
        print("product added")
        cursor.close()
        connection.close()
        

    def remove_from_cart():
        global current_user_id
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="shopping_cart" )
        cursor = connection.cursor()
        cart_product="select a.productid, a.title, a.price, a.qty from products a INNER JOIN cart_products b ON (a.productid=b.productid) where b.cartid in (select cartid from cart where userid = %s)"
        param=(current_user_id)
        cursor.execute(cart_product,param)
        records = cursor.fetchall()
        print(tabulate(records, headers=['ProductID', 'title', 'Price', 'Stock'], tablefmt='psql'))

        product_id =input("enter the comma seprated product id for removing item\n")
        pids = product_id.split(',')
        for products in pids:
            query = "Delete from cart_products where productid =%s"
            param=(products)
            cursor.execute(query,param)
            records = cursor.fetchall()
            connection.commit()
        print('Products removed')    

    def view_cart():
        global current_user_id
        cursor=user.get_connection()
        cart_product="select a.productid, a.title, a.price, a.qty from products a INNER JOIN cart_products b ON (a.productid=b.productid) where b.cartid in (select cartid from cart where userid = %s)"
        param=(current_user_id)
        cursor.execute(cart_product,param)
        records = cursor.fetchall()
        
        print(tabulate(records, headers=['ProductID', 'title', 'Price', 'Stock'], tablefmt='psql'))


    
if __name__ == "__main__":
    user.authentication()