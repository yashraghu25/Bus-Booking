from tkinter import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10,padx=(150,0))
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=Img).grid(row=0,column=0,columnspan=12)
Label(frame1,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,pady=(0,30),columnspan=12)
Label(frame1,text="Add Bus Operator Detail",font=("Arial bold",15),fg='red').grid(row=2,column=1,pady=(0,30),columnspan=12)
Label(frame1,text="Operator id",font=("Arial bold",10)).grid(row=3,column=1)
Entry(frame1).grid(row=3,column=2)
Label(frame1,text="Name",font=("Arial bold",10)).grid(row=3,column=3)
Entry(frame1).grid(row=3,column=4)
Label(frame1,text="Address",font=("Arial bold",10)).grid(row=3,column=5)
Entry(frame1).grid(row=3,column=6)
Label(frame1,text="Phone",font=("Arial bold",10)).grid(row=3,column=7)
Entry(frame1).grid(row=3,column=8)
Label(frame1,text="Email",font=("Arial bold",10)).grid(row=3,column=9,pady=30)
Entry(frame1).grid(row=3,column=10)
Button(frame1,text='Add',bg='pale green',font=("Arial bold",10)).grid(row=3,column=11,padx=10)
Button(frame1,text='Edit',bg='pale green',font=("Arial bold",10)).grid(row=3,column=12,padx=10)

homebutton=PhotoImage(file='.\\home.png')
Label(frame1,image=homebutton).grid(row=4,column=9)
Button(frame1, image=homebutton).grid(row=4,column=9)



