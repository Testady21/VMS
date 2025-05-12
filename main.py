# Central Vaccine Management System
import stock
import schedule
import password

if password.password()==True:
    print()
    print("Access granted.")
    print()
    while True:
        print('-'*105)
        print('\t\t\t\t\t  Main-Menu')
        print('-'*105)
        print("1.Vaccine stock management")
        print("2.Vaccine registration management")
        print("3.Exit")
        print('-'*105)
        print()

        choice=int(input("Enter choice : "))
        print()
       
        if choice==1:
            stock.stock()
        elif choice==2:
            schedule.schedule()
        elif choice==3:
            print("Thank You!!!")
            print()
            break
        else:
            print("Invalid response.Please Try Again")
            print()
else:
    print("Invalid password. Access denied")
