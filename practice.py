from tkinter import *
from tkinter.messagebox import *
import sqlite3
conn = sqlite3.Connection('employee')
cur = conn.cursor()
cur.execute('create table if not exists employees (eno number primary key,name varchar(20))')


class test:
    def home(self):
        def clk():
            s1=e1.get()
            s2=e2.get()
            if(len(s1)==0 or len(s2)==0):
                showerror('Error','field empty')
            else:
                cur.execute('insert into employees values(?,?)',(s1,s2))
                showinfo('info','record added')
        def clk1():
            cur.execute('select eno,name from employees')
            res=cur.fetchall()
            fr1=Frame(root)
            fr1.grid(row=2,columnspan=5)
            Label(fr1,text=res).grid(row=2,column=3)
            
        root=Tk()
        root.state('zoomed')
        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=5,padx=400,pady=200)
       
        Label(fr,text='eno',font='arial 10 bold').grid(row=0,column=0)
        e1=Entry(fr)
        e1.grid(row=0,column=1)
        Label(fr,text='Name',font='arial 10 bold').grid(row=0,column=2)
        e2=Entry(fr)
        e2.grid(row=0,column=3)
        Button(fr,text = 'insert',command = clk).grid(row = 0,column =4,padx=20)
        Button(fr,text = 'show',command = clk1).grid(row = 0,column =5)
    def next(event):
        root.destroy()
        import front
 root.bind("<KeyPress>", next)    
    def front(self):
         root=Tk()
         root.state('zoomed')
         fr=Frame(root)
         fr.grid(row=0,column=0,columnspan=5,padx=400,pady=200)
       
         Label(fr,text='eno',font='arial 10 bold').grid(row=0,column=0)
         e1=Entry(fr)
         e1.grid(row=0,column=1)
         Label(fr,text='Name',font='arial 10 bold').grid(row=0,column=2)
         e2=Entry(fr)
         e2.grid(row=0,column=3)
         Button(fr,text = 'insert',command = clk).grid(row = 0,column =4,padx=20)
         Button(fr,text = 'show',command = clk1).grid(row = 0,column =5)
t=test();
t.home()
                
        

