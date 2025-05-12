# Schedule of vaccinations
from tabulate import tabulate
import mysql.connector as x
import stock

connect=x.connect(host='localhost',user='root',password='adv123')
if connect.is_connected():
    cur=connect.cursor()
    query='create database if not exists cvms;'
    cur.execute(query)
    query='use cvms;'
    cur.execute(query)
    query='''create table if not exists scheduled(candidate_number 
    varchar(20),
    name_of_candidate char(30),
    name_of_vaccine varchar(50),
    age int(20),
    sex char(20),
    phone_no varchar(20),
    date_of_vaccination date)'''
    cur.execute(query)
    query='''create table if not exists finished(candidate_number      
    varchar(20),
    name_of_candidate char(30),
    name_of_vaccine varchar(50),
    age int(10),
    sex char(10),
    phone_no varchar(20),
    date_of_vaccination date)'''
    cur.execute(query)

def schedule():
    while True:
        print('-'*105)
        print("\t\t\t\t\tSub-Menu : Schedule")
        print('-'*105)
        print("1.New registration for vaccination")
        print("2.Display registration details of all candidates")
        print("3.Display details of indivisual candidate ")
        print("4.Vaccination of candidate completed successfully")
        print("5.Display details of all vaccinated candidates")
        print("6.No of candidates vaccinated arranged by vaccine name")
        print("7.Upcoming vaccinations")
        print("8.Go back to main menu")
        print('-'*105)
        print()

        choice=int(input("Enter choice : "))

        if choice==1:
            cnumber=input("Enter candidate number : ")
            name=input("Enter name of candidate : ")
            vname=input("Enter name of vaccine used : ")
            age=int(input("Enter age of candidate : "))
            sex=input("Enter sex : ")
            phone=int(input("Enter phone number of candidate : "))
            date=input("Enter date of vaccination of candidate : ")
            query="insert into scheduled values('{}','{}','{}',{},'{}',{},'{}');".format(cnumber,name,vname,age,sex,phone,date)
            cur.execute(query)
            connect.commit()
            print()

        elif choice==2:
            query='select * from scheduled;'
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Candidate Number','Candidate Name','Vaccine Name','Age',
            'Sex','Phone Number','Date of vaccination'],tablefmt='pretty'))
            print()
            
        elif choice==3:
            name=input("Enter name of candidate whose details are required : ")
            query="select * from scheduled where name_of_candidate='{}'".format(name)
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Candidate Number','Candidate Name','Vaccine Name','Age','Sex','Phone Number','Date of vaccination'],tablefmt='pretty'))
            print()
            
        elif choice==4:
            name=input("Enter name of candidate whose vaccination was completed successfully : ")
            vname=input("Enter vaccine used : ")  
            query="insert into finished select * from scheduled where name_of_candidate='{}'".format(name)
            cur.execute(query)
            query="delete from scheduled where name_of_candidate='{}'".format(name)
            cur.execute(query)
            connect.commit()
            Stock.reduce(vname)
            print()
        
        elif choice==5:
            query='select * from finished'
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Candidate Number','Candidate Name','Vaccine Name','Age','Sex','Phone Number','Date of vaccination'],tablefmt='pretty'))
            print()

        elif choice==6:
            query="select name_of_vaccine,count(name_of_vaccine) from finished group by name_of_vaccine"
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Vaccine Name', 'No of people vaccinated'],tablefmt='pretty'))
            print()
            
        elif choice==7:
            query="select * from scheduled order by date_of_vaccination"
            cur.execute(query)
            data=cur.fetchall()
            print(tabulate(data,headers=['Candidate Number','Candidate Name','Vaccine Name','Age','Sex','Phone Number','Date of vaccination'],tablefmt='pretty'))
            print()
            
        elif choice==8:
            print()
            break    
        else:
            print("Invalid choice. Please try again")
            print()
