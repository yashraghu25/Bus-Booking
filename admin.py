from tkinter import *
from tkinter.messagebox import *
import sqlite3
conn = sqlite3.Connection('employee')
cur = conn.cursor()
cur.execute('create table if not exists employees (sno number primary key,name varchar(20))')


class test:
       
    def front(self):
        def clk(e = 0):
            s1 = e1.get()
            s2 = e2.get()
            if(len(s1) == 0 or len(s2) == 0):
                showerror('Error','field cant remain empty')
                if s2.isnumeric():
                    showerror('Error','name should not be numeric')
                else:
                    cur.execute('insert into employees values (?,?)',(s1,s2))
                    showinfo('info','item is added')
    
                    
            else:
                cur.execute('insert into employees values (?,?)',(s1,s2))
                showinfo('info','item is added')

        def clk1(e = 0):
            cur.execute('select * from employees')
            res = cur.fetchall()
            con.commit()
            Label(root,text = res).grid(row = 1,column =0) 
        root = Tk()
        root.state('zoomed')
        root.config(background = 'light green')
        Label(root,text = 'sno').grid(row = 0,column = 0)
        e1 = Entry(root)
        e1.grid(row = 0,column = 1)
        Label(root,text = 'name').grid(row = 0,column = 2)
        e2 = Entry(root)
        e2.grid(row = 0,column = 3)
       

        Button(root,text = 'insert',command = clk).grid(row = 0,column =4)
        Button(root,text = 'show',command = clk1).grid(row = 0,column =5)
        
        def next(e=0):
            root.destroy()
            self.home()
        Button(root,text='next',command=next).grid(row=0,column=6)
    
        
    def home(self):
        def clk():
            root.destroy()
            self.front()
        root = Tk()
        root.state('zoomed')
        root.config(background = 'light blue')
        Label(root,text = 'sno').grid(row = 0,column = 0)
        e1 = Entry(root)
        e1.grid(row = 0,column = 1)
        Label(root,text = 'name').grid(row = 0,column = 2)
        e2 = Entry(root)
        e2.grid(row = 0,column = 3)
        Button(root,text = 'submit').grid(row = 0,column =4)
        Button(root,text = 'Back',command = clk).grid(row = 0,column =5)
t = test();
t.front()
