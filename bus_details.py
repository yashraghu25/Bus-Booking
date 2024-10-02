from tkinter import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=12,padx=(90,0))
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=Img).grid(row=0,column=0,columnspan=15,padx=10)
Label(frame1,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,pady=(0,30),columnspan=12)
Label(frame1,text="Add Bus Detail",font=("Arial bold",15),fg='red').grid(row=2,column=1,pady=(0,30),columnspan=12)
Label(frame1,text="Bus ID",font=("Arial bold",10)).grid(row=3,column=0)
Entry(frame1).grid(row=3,column=1)
Label(frame1,text="Bus Type",font=("Arial bold",10)).grid(row=3,column=2)
Bus_type=StringVar()
option=['NON AC 2X2','AC 2X2','NON AC 3x2','AC SLEEPER 2X1']
d=OptionMenu(frame1,Bus_type,*option)
d.grid(row=3,column=3)
Label(frame1,text="Capacity",font=("Arial bold",10)).grid(row=3,column=4)
Entry(frame1).grid(row=3,column=5)
Label(frame1,text="Fare Rs",font=("Arial bold",10)).grid(row=3,column=6,pady=30)
Entry(frame1).grid(row=3,column=7,pady=30,padx=(0,10))
Label(frame1,text="Operator ID",font=("Arial bold",10)).grid(row=3,column=8,pady=30)
Entry(frame1).grid(row=3,column=9)
Label(frame1,text="Route ID",font=("Arial bold",10)).grid(row=3,column=10)
Entry(frame1).grid(row=3,column=11)
Button(frame1,text='Add Bus',bg='pale green',font=("Arial bold",10)).grid(row=5,column=6,padx=10)
Button(frame1,text='Edit Bus',bg='pale green',font=("Arial bold",10)).grid(row=5,column=7,padx=10)
homebutton=PhotoImage(file='.\\home.png')
Label(frame1,image=homebutton).grid(row=5,column=8)
Button(frame1, image=homebutton).grid(row=5,column=8)







