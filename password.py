import random
b=''
def password():
    global b
    n=random.randint(10,30)
    for x in range(n):
        a=random.randint(65,122)
        b+=chr(a)
    file=open("pword.txt","w")
    file.write("Password - ")
    file.write(b)
    file.close()
    z=input("Enter password : ")
    if z==b:
        return True
    else:
        return False
