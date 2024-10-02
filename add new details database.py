from tkinter import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10,padx=w/4)
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=Img).grid(row=0,column=0,columnspan=12)
Label(frame1,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,pady=(0,30),columnspan=12)
Label(frame1,text="Add New Details to Database",font=("Arial bold",15),fg='red').grid(row=2,column=1,pady=(0,30),columnspan=12)
Button(frame1,text='New Operator',font=("Arial bold",12),bg='spring green').grid(row=3,column=1,padx=(0,30))
Button(frame1,text='New Bus',font=("Arial bold",12),bg='orange').grid(row=3,column=2,padx=30)
Button(frame1,text='New Route',font=("Arial bold",12),bg='medium orchid').grid(row=3,column=3,padx=30)
Button(frame1,text='New Run',font=("Arial bold",12),bg='plum3').grid(row=3,column=4,padx=30)





