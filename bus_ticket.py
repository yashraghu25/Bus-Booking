from tkinter import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10,padx=w/3)
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=Img).grid(row=0,column=0,columnspan=12)
Label(frame1,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,pady=(0,20),columnspan=12)
Label(frame1,text='Bus Ticket',font='arial 12 bold').grid(row=2,column=1,columnspan=12)
fr2=Frame(root)
fr2.grid(row=1,columnspan=10,padx=30)
