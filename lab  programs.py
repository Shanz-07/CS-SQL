
#PROGRAM_01 -> *WAP using function lshift(lst,n) in Python which accepts a 
# list of numbers and n is the numeric value by which all elements of the list is shifted to left.
'''
n=int(input("Enter the no of elements to shift left"))
lst=eval(input("Enter list: "))
def lshift(lst,n):
    length=len(lst)
    for x in range(n):
        a=0
        start=lst[0]
        for i in range(length-1):  
            lst[a]=lst[a+1]
            a+=1
        lst[length-1]=start
    print(lst)
lshift(lst,n)

#PROGRAM_02 ->  WAP using the function that takes 2 numbers and returns the number that has minimum one’s digit
def min_one(n1,n2):
    ones_digitn1=n1%10
    ones_digitn2=n2%10
    if ones_digitn1 < ones_digitn2:
        return n1
    else:
        return n2
n1=int(input("Enter first no: "))
n2=int(input("Enter second no: "))
print(min_one(n1,n2))

#PROGRAM_03 -> WAP using function that receives two strings arguments and checks whether they are 
# same length string (Returns True in this case else False).
def string_length(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1==l2:
        return True
    else:
        return False
s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
print(string_length(s1,s2))

#PROGRAM_04 -> WAP using function that generate a series using a function which takes first and last values of the
#  series and generate four terms that are equidistant.
def series(s1,e1):
    step=(e1-s1)//3
    serie=[s1,s1+step,s1+2*step,e1]
    return serie
s1=int(input("Enter the first element: "))
e1=int(input("Enter the last element: "))
print(series(s1,e1))


#PROGRAM_05 -> Write a menu driven program using function to
# (i)generate Fibonacci series between 1 to 200 (0,1,1,2,3,5,8,13,21………)
# (ii) Write a program to find factorial of a number.

def fibonacci_generator_or_factorial():
    print('generate fibonacci series from 0 to 200 (click A):'
            'Find factorial of a no (click B):')
    x=input()
    if x=='a':
        first=0
        sec=1
        print(first,end=' ')
        print(sec,end=' ')
        while True:
            n1=first+sec
            if first<sec:
                first=sec
                sec=n1
            else:
                sec=first
                first=n1
            if n1>=200:
                break
            print(n1,end=' ')
    if x=='b':
        n=int(input("Enter the no to find factorial: "))
        for i in range(n-1):
            n*=i+1
        print(n) 
fibonacci_generator_or_factorial()

#PROGRAM_06 -> Write a program using function to read a file and count the words “to” and “the” present in the text file.

file1=open('lab program\p6.txt','r')
data=file1.read()
words=data.split()
x=0
for i in words:
    if i=='to' or i == 'the':
        x+=1
print(x)


#PROGRAM_07 -> WAP to read a text file and create another file that is identical except every blank/space is replaced by a comma.

file1=open('lab program\p7.txt','r+')
data=file1.read()
print(data)
new_data=data.replace(' ',',')
file1.seek(0)
file1.write(new_data)
file1.close()


#PROGRAM_08 -> WAP using function to read lines and display those lines which are starting either with ‘A’or ‘E’.

file1=open('lab program\p8.txt','r+')
data=file1.read()
words=data.splitlines()
for i in words:
    if i[0]=='A' or i[0]=='E':
        print(i)


#PROGRAM_09 -> WAP to display the size of a file after removing EOL characters, leading and trailing white 
#spaces and blank lines.

file1=open('lab program\p9.txt','r+')
data=file1.read()
print(data)
for i in data:
    if i ==' ':
        data=data.strip()
file1.close()
file1=open('lab program\p9.txt','w')
file1.write(data)
file1.close()



#PROGRAM_10 ->WAP to get the roll numbers, names and marks of the 3 students of a class(get from theuser) 
# and store these details in a file called “Marklist.txt” .
file1=open('Marklist.txt','w')
for i in range(3):
    rno=input("Enter the roll no of the student: ")
    name=input("Enter the name of the student: ")
    marks=input("Enter the marks: ")
    file1.write(rno+' '+name+' '+marks+'\n')
file1.close()


#PROGRAM_11 -> WAP to create a binary file:” student.dat” and write into it the students’ details - roll_no,
# name, marks. Read and display the students’ records stored in it.
import pickle
file1=open('lab program\student.dat','wb+')
n=int(input("Enter the no of students: "))
for i in range(n):
    rno=int(input("Enter your roll no: "))
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    student_data=[rno,name,marks]
    pickle.dump(student_data,file1)
file1.seek(0)
while True:
    try:
        data=pickle.load(file1)
        print(f"rno: {data[0]},name: {data[1]},marks: {data[2]}")
    except EOFError:
        break
file1.close()

#PROGRAM_12 -> WAP to Read the file “student.dat” created in the previous program and update the
# records for those who have scored more than 80 get additional bonus of 5.
import pickle
file1=open('lab program\student.dat','rb')
students=[]
while True:
    try:
        data=pickle.load(file1)
        if data[2]>=80:
            data[2]+=5
        students.append(data)
        print(data)
    except EOFError:
        break
file1.close
file1=open('lab program\student.dat','wb')
for i in students:
    pickle.dump(i,file1)
file1.close()

#PROGRAM_13 -> WAP to create a CSV file “result.csv” and write rollno, name, marks, grade of students
# into it. Read the file and display the records.
import csv
file1=open('lab program\student.dat','w+',newline='')
writer=csv.writer(file1)
writer.writerow(['rno','name','marks','grade'])
n=int(input("Enter the no of students"))
for i in range(n):
    rno=int(input("Enter your roll no: "))
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    grade=input("Enter your grade: ")
    writer.writerow([rno,name,marks,grade])
reader=csv.reader(file1)
print(reader)


#PROGRAM_14 -> Writing a python program to implement stack operations push pop and display using List.
stack=[]
def push():
    e=int(input("Enter your element to be pushed: "))
    stack.append(e)
def pop():
    stack.pop()  
def display():
    print(stack)
while True: 
    print("Which operation do you want to proceed: \n1) push: (press 1)\n2) pop: (press 2)\n3) display: (press 3)\n4) exit: (press 4) ")
    x=int(input())
    if x == 1:
        push()
    if x==2:
        pop()
    if x==3:
        display()
    if x==4:
        break

#PROGRAM_15 ->  Writing a Python program for push(0 and pop() method using the following informations:-
# pincode, ii) city
stack=[]
def push():
    pincode=int(input("Enter your pincode: "))
    city=input("Enter your city name: ")
    entry={'pincode':pincode,'city':city}
    stack.append(entry)
def pop():
    stack.pop()
def display():
    print(stack)
while True:
    print("Which operation do you want to proceed: \n1) push: (press 1)\n2) pop: (press 2)\n3) display: (press 3)\n4) exit: (press 4) ")
    x=int(input())
    if x == 1:
        push()
    if x==2:
        pop()
    if x==3:
        display()
    if x==4:
        break
 
----------------------------------------------------------------------------------------------------------------------------------------------------------

#SQL - QUERIES
Consider the tables dept and emp below and write the queries for the following Dept emp

Query1- To create the tables Dept and emp.
Query2- To insert the values in the tables.
Query3- Add a new attribute date_of_join to the table emp and insert the appropriate
value for the same.
Query4-Display the details of department who’s head name ends with letter ‘a’.
Query5-Display maximum, minimum, average and sum of the salaries of the employees
in each department in descending order of salary from emp table.
Query6-Display department wise the number of employees from emp table having count
more than one.
Query7- Display department number, department name and salary of all the employees.
Query8 - List the employee having salary more than 100000 and working in Production
department.
Query9 - Increment the salary of all the employees of Sales department.
Query 10- Delete the record of the employee who is not receiving the salary from emp
table.

Query - 01: 
1)create table Dept(deptno INT(50),dname varchar(50),dhead varchar(50));
2)create table emp(empno int(50),ename varchar(50),deptno int(50),salary int(50));

Query - 02:
1) insert into Dept VALUES(10,'Sales','Ritika');
   insert into Dept VALUES(20,'HR','Ankit');
   insert into Dept VALUES(30,'Production','Abuzair');
   insert into Dept VALUES(40,'IT','Mesha');

2) insert into emp VALUES(1,'Alam',10,11924);
   insert into emp VALUES(2,'Srijeeta',20,9450);
   insert into emp VALUES(3,'Bhaskar',30,118986);
   insert into emp VALUES(4,'Rita',10,13892);
   insert into emp VALUES(5,'Riyan',20,null);

Query - 03:
alter table emp
add column date_of_join date;

Query-04:
select * from dept where dhead like '%a';

Query-05:
select max(salary),min(salary),avg(salary),sum(salary) from emp order by salary desc

Query-06:
SELECT d.dname, COUNT(e.empno) AS employee_count
FROM emp e 
JOIN dept d ON e.deptno = d.deptno
GROUP BY d.dname
HAVING COUNT(e.empno) > 0;

Query-07:
SELECT e.deptno, d.dname, e.salary
FROM emp e
JOIN dept d ON e.deptno = d.deptno;

Query-08:
SELECT e.empno, e.ename, e.salary, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE e.salary > 100000 AND d.dname = 'Production';

Query-09:
UPDATE emp e
JOIN dept d ON e.deptno = d.deptno
SET e.salary = e.salary + (e.salary * 0.10)
WHERE d.dname = 'Sales';

Query-10:
DELETE FROM emp
WHERE salary IS NULL;

 
Write a program to connect Python with MySQL using database connectivity and 
perform the following operations on data in database: Insert, Fetch, Update and 
delete the data 
 
 
Program 1- Create a table Dept 
Program2 – Insert the data in the table. 
Program 3- Fetch and display the data.  
Program4- Change the dname to Management whose head is Ankit. 
Progarm5- Delete the record of IT department.


import mysql.connector as mysqlctr
mycon=mysqlctr.connect(user='root',password='',host='localhost',database='neww',auth_plugin='mysql_native_password')
if mycon.is_connected:
    print("Success")
cursor=mycon.cursor()
cursor.execute('Create table Dept(deptno INT(50),dname varchar(50),dhead varchar(50))')
cursor.execute("Insert into Dept VALUES(10,'Sales','Ritika')")
cursor.execute("Insert into Dept VALUES(20,'HR','Ankit')")
cursor.execute("Insert into Dept VALUES(30,'Production','Abuzair')")
cursor.execute("Insert into Dept VALUES(40,'IT','Mesha')")
cursor.execute("Update dept set dname='Management' where dhead='Ankit' ")
cursor.execute("Delete from dept where dname='IT'")
cursor.execute("SELECT * FROM Dept")
data=cursor.fetchall()
print(data)
mycon.commit()
'''
