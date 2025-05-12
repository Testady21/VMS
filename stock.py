# stock management system
from tabulate import tabulate
import mysql.connector as x


connect=x.connect(host='localhost',user='root',password='adv123')
if connect.is_connected():
    cur=connect.cursor()
    query='create database if not exists cvms;'
    cur.execute(query)
    query='use cvms;'
    cur.execute(query)
    query='''create table if not exists stock(vaccine_number   
    varchar(20),
    vaccine_name varchar(50),
    supplier varchar(50),
    country_of_origin char(20),
    quantity int(10),
    price float(20,4));'''
    cur.execute(query)


def stock():
    while True:
        print('-'*105)
        print("\t\t\t\t\tSub-Menu: Stock")
        print('-'*105)
        print("1.Add consignement of vaccines")
        print("2.Display details of all vaccines")
        print("3.Display details of a paticular vaccine")
        print("4.Delete indivisual vaccine record")
        print("5.Display total number of vaccines in stock")
        print("6.Update number of a partcular in stock")
        print("7.Go back to main menu")
        print('-'*105)
        print()

        choice=int(input("Enter choice : "))

        if choice==1:
            vname=input("Enter name of vaccine : ")
            vnumber=input("Enter vaccine number : ")
            supplier=input("Enter supplier name : ")
            coo=input("Enter country of origin : ")
            quantity=int(input("Enter number of vaccines : "))
            price=int(input("Enter price of each vaccine : "))
            query="insert into stock values('{}','{}','{}','{}',{},{});".format(vnumber,vname,
            supplier,coo,quantity,price)
            cur.execute(query)
            connect.commit()
            print()

        elif choice==2:
            query='select * from stock'
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Vaccine number','Vaccine name','Supplier','Country Of Origin','Quantity','Price'],tablefmt='pretty'))
            print()
            
        elif choice==3:
            vname=input("Enter name of vaccine whose details are required : ")
            query="select * from stock where vaccine_name='{}'".format(vname)
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Vaccine number','Vaccine name','Supplier','Country Of Origin','Quantity','Price'],tablefmt='pretty'))
            print()
            
        elif choice==4:
            vname=input("Enter name of vaccine whose records are to be deleted : ")
            query="delete from stock where vaccine_name='{}'".format(vname)
            cur.execute(query)
            connect.commit()
            print()
        
        elif choice==5:
            query="select sum(quantity) as 'Total Number Of Vaccines In Stock' from stock"
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Total Numuber Of Vaccines In Stock'],tablefmt='pretty'))
            print()

        elif choice==6:
            vname=input("Enter name of vaccine : ")
            n=int(input("Enter updated quantity of vaccine : "))
            query="update stock set quantity={} where vaccine_name='{}'".format(n,vname)
            cur.execute(query)
            connect.commit()
            print()
            
        elif choice==7:
            print()
            break
        
        else:
            print("Invalid choice. Please try again")
            print()
            
def reduce(vname):
    query="update stock set quantity=quantity-1 where vaccine_name='{}'".format(vname)
    cur.execute(query)
    connect.commit()
