import sqlite3
from goto import label,goto
import re
item=['Bikes','Cycle','Car','Boat']
amnt=[2,3,1,2]
scon=sqlite3.connect('VEHICLE.db')
cur=scon.cursor()
table='''DROP TABLE IF EXISTS Inventory'''
cur.execute(table)
table='''CREATE TABLE IF NOT EXISTS Inventory(Name text UNIQUE,Quantity Integer);'''
cur.execute(table)
insert="INSERT INTO Inventory(Name,Quantity)VALUES(?,?)"
for i in range(0,4):
    cur.execute(insert,(item[i],amnt[i]))
scon.commit()
scon.close()
def Menu():
        ch='0'
        print(" Menu ")
        print(" 1-Add Customer ")
        print(" 2-Add Rental Booking ")
        print(" 3-See Customer List ")
        print(" 4-See Rental Booking List ")
        print(" 5-See Inventory ")
        print('enter 6 to exit')
        print('ENTER CHOICE')
        ch=input()

        if ch=='1':
            v.addcustom()
        if ch=='2':
            v.addbooking()
        if ch=='3':
            v.dispCustom()
        if ch=='4':
            v.dispBooking()
        if ch=='5':
            v.dispI()
        

            
class Vehicle:
    def addcustom():
        f=0
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        c=input('Enter your Name')
        n=input('Enter Mobile Number')
        e=''
        while f==0:
            e=input('Please Enter your Email')
            if(re.fullmatch(regex, e)):
                f=1
                print('welcome user u r now registered')
            else:
                print('enter valid email')
                f=0
        
        try:
            scon=sqlite3.connect('VEHICLE.db')
            cur=scon.cursor()
            table='''CREATE TABLE IF NOT EXISTS Customer(Name text Not Null,Phone text Not Null,Email text Unique);'''
            insert="INSERT INTO Customer(Name,Phone,Email)VALUES(?,?,?)"
            cur.execute(table)
            cur.execute(insert,(c,n,e))
        except Exception as e:
            print(e)
        scon.commit()
        scon.close()
        Menu()

    def dispI():
        print(" items Currently available ")
        try:
            scon=sqlite3.connect('VEHICLE.db')
            cur=scon.cursor()
            col='''SELECT * FROM Inventory'''
            cur.execute(col)
            ser=cur.fetchall()
            for i in ser:
                print(i[0],i[1])
        except Exception as e:
            print(e)
        scon.commit()
        scon.close()
        Menu()

    def dispCustom():
        print('Customer List')
        try:
            scon=sqlite3.connect('VEHICLE.db')
            cur=scon.cursor()
            table='''select * from Customer'''
            cur.execute(table)
            ser=cur.fetchall()
            for i in ser:
                print(i)
        except Exception as e:
            print(e)
        scon.commit()
        scon.close()
        Menu()

    def addbooking():
        cus=input('enter name')
        try:
            scon=sqlite3.connect('VEHICLE.db')
            cur=scon.cursor()
            table='''Select * From Customer Where Name=?'''
            cur.execute(table,(cus,))
            ser=cur.fetchall()
            if ser !='':
                ta='''CREATE TABLE IF NOT EXISTS Bookings(Name text Not NULL,rental_date text,return_date text Not NULL,Vehicle text);'''
                ##label.again
                veh=input('Enter the vehicle you need')
                ta1='''Select Quantity From Inventory Where Name=?'''
                cur.execute(ta1,(veh,))
                amt=cur.fetchone()
                if amt==0:
                    print('SORRY Vehicle Not available')
                    Menu()
                    ##goto.again
                else:
                    cur.execute(ta)
                    rent=input('Enter rental date')
                    ret=input('Enter return date')
                    que="Insert INTO Bookings(Name,rental_date,return_date,Vehicle)VALUES(?,?,?,?)"
                    cur.execute(que,(cus,rent,ret,veh))
                    up=('''UPDATE Inventory SET Quantity=Quantity-1 WHERE Name=?;''')
                    cur.execute(up,(veh,))
            else:
                print('You are not register')
                Menu()
        except Exception as e:
            print(e)
            Menu()
        scon.commit()
        scon.close()
        Menu()

    def dispBooking():
        try:
            scon=sqlite3.connect('VEHICLE.db')
            cur=scon.cursor()
            table='''select * from Bookings'''
            cur.execute(table)
            ser=cur.fetchall()
            print(ser)
        except Exception as e:
            print(e)
        scon.commit()
        scon.close()
        Menu()
    
if __name__=='__main__':
        v=Vehicle
        Menu()


        





