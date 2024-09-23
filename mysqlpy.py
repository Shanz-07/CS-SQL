#MySQL-Python
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd="",database="cs")
if mycon.is_connected():
    print("Succesfully connected to mysql database")
cursor=mycon.cursor()

def modify_column():
    selection=input("Enter the name of the column you want to modify: ")
    datatype=input("enter the datatype")
    cursor.execute("ALTER TABLE cspractice MODIFY COLUMN {} {}".format(selection,datatype))
    mycon.commit()
    row=cursor.fetchall()
    for i in row:
        print(i)

def modify_quantity():
    sub_name=input("Enter the subject name to rename its qty value: ")
    newval=input("Enter the quantity value for it: ")
    cursor.execute("UPDATE cspractice SET QUANTITY=%s WHERE SUBJECT=%s",(newval,sub_name))
    mycon.commit()
    row=cursor.fetchall()
    for i in row:
        print(i)

def delete_row():
    sub=input("Enter the subject you want to delete: ")
    cursor.execute("DELETE FROM cspractice WHERE SUBJECT=%s",(sub,))
    mycon.commit()
    print("Row deleted successfully")

def add_row():
    sn,sub,book,qty=input("Enter the sno,sub,book and qty seperated by spaces: ").split()
    cursor.execute("INSERT INTO cspractice VALUES(%s,%s,%s,%s)",(sn,sub,book,qty))
    mycon.commit()
    print("Row added successfully")
add_row()
    
