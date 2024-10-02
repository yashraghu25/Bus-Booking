from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=12,padx=150)
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=Img).grid(row=0,column=1,columnspan=12)
Label(frame1,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,pady=(0,30),columnspan=12)
Label(frame1,text="Enter Journey Details",font=("Arial bold",15),bg='pale green',fg='red').grid(row=2,column=1,columnspan=12,pady=(0,30))
Label(frame1,text="To",font=("Arial bold",10)).grid(row=3,column=0,padx=20,pady=20)
Entry(frame1).grid(row=3,column=1)
Label(frame1,text="From",font=("Arial bold",10)).grid(row=3,column=2,padx=20)
Entry(frame1).grid(row=3,column=3)
Label(frame1,text="Journey Date",font=("Arial bold",10)).grid(row=3,column=4)
Entry(frame1).grid(row=3,column=5)

def bus():
    fr2=Frame(root)
    fr2.grid(row=4,columnspan=12,padx=90)
    Label(fr2,text='Select bus',fg='red',font=('arial bold',12)).grid(row=4,column=0)
    Label(fr2,text='Operator',fg='red',font=('arial bold',12)).grid(row=4,column=1,padx=30)
    Label(fr2,text='Bus Type',fg='red',font=('arial bold',12)).grid(row=4,column=2,padx=20)
    Label(fr2,text='Available/Capacity',fg='red',font=('arial bold',12)).grid(row=4,column=3,padx=20)
    Label(fr2,text='Fare',fg='red',font=('arial bold',12)).grid(row=4,column=4,padx=30)
    fr3=Frame(root)
    fr3.grid(row=7,columnspan=12,padx=90)
    def passengerdetails():
        Label(fr3,text="Fill Passenger Details To Book The Bus Ticket",fg='red',font=("Arial bold",20),bg='light blue').grid(row=7,column=1,pady=20,columnspan=12)
        Label(fr3,text='Name',font=('arial bold',10)).grid(row=8,column=0)
        Entry(fr3).grid(row=8,column=1)
        Label(fr3,text='Gender',font=('arial bold',10)).grid(row=8,column=3)
        gender=StringVar()
        option=['Male','Female','Third gender']
        d=OptionMenu(fr3,gender,*option)
        d.grid(row=8,column=4)
        Label(fr3,text='No. of Seats',font=('arial bold',10)).grid(row=8,column=5)
        Entry(fr3).grid(row=8,column=6)
        Label(fr3,text='Mobile No.',font=('arial bold',10)).grid(row=8,column=7)
        Entry(fr3).grid(row=8,column=8)
        Label(fr3,text='Age',font=('arial bold',10)).grid(row=8,column=9)
        Entry(fr3).grid(row=8,column=10)
        def check():
            askyesno('Fare Confirm ','Total amount to be Paid ')
        Button(fr3,text='Book Seat',command=check,bg='pale green',font=("Arial bold",12)).grid(row=8,column=11,padx=20)
   
    Button(fr2,text='Proceed to Book',command=passengerdetails,bg='pale green',font=("Arial bold",12)).grid(row=5,column=7,pady=20)

Button(frame1,text='Show Bus',command=bus,bg='pale green',font=("Arial bold",10)).grid(row=3,column=7,padx=20)
homebutton=PhotoImage(file='.\\home.png')
Label(frame1,image=homebutton).grid(row=3,column=8)
Button(frame1, image=homebutton).grid(row=3,column=8)









